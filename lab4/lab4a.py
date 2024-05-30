end_ing = {0:{'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 1,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0},
    1:{'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 1,'j': 0,'k': 0,'l': 0,'m': 0,'n': 2,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0},
    2:{'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 3,'h': 0,'i': 1,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0},
    3:{'a': 1,'b': 1,'c': 1,'d': 1,'e': 1,'f': 1,'g': 1,'h': 1,'i': 1,'j': 1,'k': 1,'l': 1,'m': 1,'n': 1,'o': 1,'p': 1,'q': 1,'r': 1,'s': 1,'t': 1,'u': 1,'v': 1,'w': 1,'x': 1,'y': 1,'z': 1},
}


def accepts(transition,start,end, string):
    state = start
    for character in string:
        state = transition[state][character]
    if state == end:
        return True

string = input('Enter a string: ')
if (accepts(end_ing,0,3,string)):
    print("Accepts")
else:
    print("Rejects")

        
  