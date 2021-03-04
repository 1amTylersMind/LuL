import random, sys, os 

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
		   'n','o','p','q','r','s','t','u','v','w','x','y','z']

def create_random_filename(ext):
	return ''.join(random.sample(letters, 8))+ext


def reveal(n):
	print(n)
	return n

def parse(f,d):
	out = []
	for ln in open(f,'r').readlines():	out.append(ln)
	if d:	os.remove(f)
	return out


def main():
	if '-lol' in sys.argv:
		os.system('python %s -lol' % sys.argv[0])
	name = sys.argv[0]
	showandtell = lambda s : reveal(s)
	this = ''.join(parse(name, True))
	os.system('echo "'+showandtell(this)+ '" >> ' + create_random_filename('.py'))

if __name__ == '__main__':
	main()
