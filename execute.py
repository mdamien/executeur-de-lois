import sys

file = sys.argv[1]

article = None
instruction = None
for line in open(file):
    if line.startswith('Article "):
        article = int(line.split()[-1])
        print("article(%s)" %s article)
        continue
    else:
        if "il est ajouté un alinéa ainsi rédigé" in line:
            print("mode('inserer')")
