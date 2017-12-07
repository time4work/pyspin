import popen2

class hunspell:
    def __init__(self):
        self._f = popen2.Popen3("hunspell")
        self._f.fromchild.readline() #skip the credit line
    def __call__(self, words):
        words = words.split(' ')
        output = []
        for word in words:
            self._f.tochild.write(word+'\n')
            self._f.tochild.flush()
            s = self._f.fromchild.readline().strip().lower()
            self._f.fromchild.readline() #skip the blank line
            if s == "*":
                output.append(None)
            elif s[0] == '#':
                output.append("No Suggestions")
            elif s[0] == '+':
                pass
            else:
                output.append(s.split(':')[1].strip().split(', '))
        return output
h = hunspell()
print( h('After stroking her mans cock and sucking it in really hot manners, brunette porn model with big tits, Yu Shinohara, began spreading her legs, inviting the guy to deep lick her cherry and then fuck it in hardcore, craving for jizz on her shaved Asian pussy in the end.') )