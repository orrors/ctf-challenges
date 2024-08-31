nodes = dict()

def add_edge(a,b,v):
	if a in nodes: nodes[a].append((b,v))
	else: nodes[a] = [(b,v)]

with open('deterministic.clean.txt') as f:
	for l in f:
		l = l.split()
		a,b,v = int(l[0]), int(l[2]), l[1]
		if len(v) == 1 and v[0] in '0123456789':
			v=f'0{v}'
		add_edge(a,b,v)

def decode(flag):
# through some trial and error I noticed that this sample result
# 33614318932829893693299354933693299354932790544728602839549374554398929544588154788
# would decode to
# HTB{4ut0M4t4_4r3_FuUuN_4nD_N0t_D1fF1
# using the value 105 to XOR each number
	return ''.join(chr(int(flag[:-1][c:c+2])^105) for c in range(0,len(flag)-1,2)) + '}'

def dfs(i, flag=""):
	if len(flag)>1 and flag[-1] == "}":
		if 'M4t4_4M4t4' not in decode(flag):
			print(decode(flag))
		return
	try:
		for e in nodes[i]:
			dfs(e[0], flag+e[1])
	except KeyError:
		if 'M4t4_4M4t4' not in decode(flag):
			print(decode(flag))
		pass
	except RecursionError: pass
dfs(0)


