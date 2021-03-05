import random, sys, os 

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
		   'n','o','p','q','r','s','t','u','v','w','x','y','z']

def create_random_filename(ext):
	return ''.join(random.sample(letters, 8))+ext


def reveal(n):
	print(n) # Add things above and they will print to console (ascii art, whatever...)
	return n

def parse(f,d):
	out = []
	for ln in open(f,'r').readlines():	out.append(ln)
	if d:	os.remove(f)
	return out


def main():
	name = sys.argv[0]
	showandtell = lambda s : reveal(s)
	this = ''.join(parse(name, True))
	if os.name != 'nt':
		os.system('echo "'+showandtell(this)+ '" >> ' + create_random_filename('.py'))
	else:
		open(create_random_filename('.py'),'w').write(showandtell(this))
		os.system('python %s' % sys.argv[0])
if __name__ == '__main__':
	main()
