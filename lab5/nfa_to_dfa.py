import pandas as pd

nfa = {'A': {'0': ['A','B'], '1': ['A']}, 'B': {'0': [], '1': ['C']}, 'C': {'0': [], '1': []}}
# n = int(input("No. of states : "))
# t = int(input("No. of transitions : "))
t = 2
# for i in range(n):
#     state = input("state name : ")
#     nfa[state] = {}
#     for j in range(t):
#         path = input("path : ")
#         print("Enter end state from state {} travelling through path {} : ".format(state, path))
#         reaching_state = [x for x in input().split()]
#         nfa[state][path] = reaching_state

print("\nNFA :- \n")
print(nfa)
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]
# print(nfa_final_state)

new_states_list = []
dfa = {}
keys_list = list(list(nfa.keys())[0])
# print(keys_list)
path_list = list(nfa[keys_list[0]].keys())
# print(path_list)

dfa[keys_list[0]] = {}
for y in range(t):
    # print(dfa)
    var = "".join(nfa[keys_list[0]][
                      path_list[y]])
    # print(var)
    dfa[keys_list[0]][path_list[y]] = var
    # print("-",dfa)
    if var not in keys_list:
        new_states_list.append(var)
        keys_list.append(var)
# print(keys_list)

while len(new_states_list) != 0:
    dfa[new_states_list[0]] = {}
    # print(new_states_list)
    # print("dfa-",dfa)
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]
            # print("temp",temp)
            s = ""
            s = s.join(temp)
            # print("s",s)
            if s not in keys_list:
                new_states_list.append(s)
                keys_list.append(s)
            dfa[new_states_list[0]][path_list[i]] = s
            # print("inside while",dfa)
    new_states_list.remove(new_states_list[0])

print("\nDFA :- \n")
print(dfa)
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
# print(dfa_states_list)
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_final_states)
