#!/usr/bin/env python
import md5
import json
import random
import string

def v_print(content):
    print json.dumps(content, encoding='utf-8', ensure_ascii=False, indent=1)

def rand_str(max_len=15):
    rand_len = random.randint(5, max_len)
    return string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','#','%','^','&','*'], rand_len)).replace(' ','')

class ConsistentHash(object):
    def __init__(self, servers=None, rep=3):
        self.rep = rep
        self.key_srv_map = dict()
        self._sorted_keys = []

        for srv in servers:
            self.add_servers(srv)

    def add_servers(self, server):
        for i in xrange(0, self.rep):
            key = self.get_key('%s#%s' % (server, i))
            self.key_srv_map[key] = server
            self._sorted_keys.append(key)
        self._sorted_keys.sort()

    def remove_server(self, server):
        for i in xrange(0, self.rep):
            key = self.get_key('%s#%s' % (server, i))
            del self.key_srv_map[key]
            self._sorted_keys.remove(key)
        self._sorted_keys.sort()

    def place(self, key):
        if not self.key_srv_map:
            return None, None

        tar_key = self.get_key(key)

        for i, node in enumerate(self._sorted_keys):
            if tar_key <= node:
                return self.key_srv_map[node], i
        return self.key_srv_map[self._sorted_keys[0]], 0

    def get_key(self, key):
        m = md5.new()
        m.update(key)
        return long(m.hexdigest(), 16)

    def print_ring(self):
        print 'Replicas: %s' %self.rep
        v_print(self.key_srv_map)
        v_print(self._sorted_keys)



if __name__=='__main__':
    server_list = ['192.168.96.1:8649',
                   '192.168.96.2:8649',
                   '192.168.96.3:8649',
                   '192.168.96.4:8649',
                   '192.168.96.5:8649',
                   '192.168.96.6:8649',
                   '192.168.96.7:8649',
                   '192.168.96.8:8649']

    ch = ConsistentHash(servers=server_list, rep=3)

    cnt_dict = dict()
    #rand_sample
    rand_sample = []
    for i in xrange(0, 2000):
        rand_sample.append(rand_str(15))

    for samp in rand_sample:
        node, pos = ch.place(samp)
        if cnt_dict.has_key(node):
            cnt_dict[node] += 1
        else:
            cnt_dict[node] = 1
    print '%d servers' %len(server_list)
    v_print(cnt_dict)

    rand_rm_srv = server_list[random.randint(0, len(server_list)-1)]

    ch.remove_server(rand_rm_srv)

    cnt_dict = dict()
    for samp in rand_sample:
        node, pos = ch.place(samp)
        if cnt_dict.has_key(node):
            cnt_dict[node] += 1
        else:
            cnt_dict[node] = 1
    print 'remove: %s' %rand_rm_srv
    v_print(cnt_dict)

