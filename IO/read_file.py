from sys import argv

script, filename = argv

txt = open(filename)

print "Here is the file %r:" % filename
print txt.read()

print "Type the filename again:"
file_ = raw_input("> ")

txt_ = open(file_)

print txt_.read()
