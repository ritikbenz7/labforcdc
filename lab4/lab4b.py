comment_python={0:{'#':1,'a': 2,'b': 2,'c': 2,'d': 2,'e': 2,'f': 2,'g': 2,'h': 2,'i': 2,'j': 2,'k': 2,'l': 2,'m': 2,'n': 2,'o': 2,'p': 2,'q': 2,'r': 2,'s': 2,'t': 2,'u': 2,'v': 2,'w': 2,'x': 2,'y': 2,'z': 2},
                1:{'a': 1,'b': 1,'c': 1,'d': 1,'e': 1,'f': 1,'g': 1,'h': 1,'i': 1,'j': 1,'k': 1,'l': 1,'m': 1,'n': 1,'o': 1,'p': 1,'q': 1,'r': 1,'s': 1,'t': 1,'u': 1,'v': 1,'w': 1,'x': 1,'y': 1,'z': 1},
                2:{'#':2,'a': 2,'b': 2,'c': 2,'d': 2,'e': 2,'f': 2,'g': 2,'h': 2,'i': 2,'j': 2,'k': 2,'l': 2,'m': 2,'n': 2,'o': 2,'p': 2,'q': 2,'r': 2,'s': 2,'t': 2,'u': 2,'v': 2,'w': 2,'x': 2,'y': 2,'z': 2} }

def accepts(transition,start,end, string):
    state = start
    for character in string:
        state = transition[state][character]
    if state == end:
        return True
    
string = input('Enter a string: ')
if (accepts(comment_python,0,1,string)):
    print("Accepts")
else:
    print("Rejects")