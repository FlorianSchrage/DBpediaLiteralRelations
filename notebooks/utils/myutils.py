import pickle
import shlex

def save_object(obj, name ):
    with open('objects/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_object(name ):
    with open('objects/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


special_token = 'XXX_special_token_XXX'
def split_triple(triple):
    #lex = shlex.shlex(triple)
    #lex.quotes = '"'
    #lex.whitespace_split = True
    #lex.commenters = ''
    #split_list = list(lex)
    
    triple = triple.replace('\'',special_token)
    split_list = shlex.split(triple)
    
    try:
        a = split_list[3]
    except IndexError:
        print("Invalid Triple: " + str(split_list))
    
    if split_list[3] == '.':
        del(split_list[3])
        
    split_list = [ x.replace(special_token, '\'') for x in split_list ]
    
    if len(split_list) != 3:
        print('Invalid Split (length is ' + str(len(split_list)) +'): ' + str(split_list))
    return split_list

def short_name(long_name):
    if long_name[4] != 's':
        return long_name[28:].replace('/','___')
    else:
        return long_name[29:].replace('/','___')
    
def long_name(short_name):
    return 'http://dbpedia.org/ontology/' + short_name.replace('___','/')