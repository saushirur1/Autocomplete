class trie_node:
  def __init__(self,prefix):
     self.prefix = prefix
     self.end_of_word = False
     self.hashmap = {}

class trie:
  def __init__(self):
    self.root = None

  def insert(self,list_of_words):
    if self.root == None:
      self.root = trie_node("")
    for x in range(0,len(list_of_words)):
      word = list_of_words[x]
      current = self.root
      for y in range(0,len(word)):
        if word[y] not in current.hashmap:
          current.hashmap[word[y]] = trie_node(word[0:y+1])
        current = current.hashmap[word[y]]
      current.end_of_word = True

  def prefix_search(self,prefix_word):
      current = self.root
      for x in range(0,len(prefix_word)):
        if prefix_word[x] not in current.hashmap:
          return False
        current = current.hashmap[prefix_word[x]]
      return True

  def word_search(self,word_search):
      current = self.root
      for x in range(0,len(word_search)):
        if word_search[x] not in current.hashmap:
          return False
        current = current.hashmap[word_search[x]]
      return current.end_of_word

  def autocomplete(self,prefix):
    current = self.root
    list_of_word = []
    for x in range(0,len(prefix)):
      if prefix[x] not in current.hashmap:
        return list_of_word
      current = current.hashmap[prefix[x]]
    self.recursive_helper(list_of_word,current)
    return list_of_word

  def recursive_helper(self,list_of_word,current):
    if current.end_of_word == True:
      list_of_word.append(current.prefix)
    for key,values in current.hashmap.items():
        self.recursive_helper(list_of_word,current.hashmap[key])

def main():
  list1 = ["yellow","yell","yello","hey","yuy","iuoi","how","howare","hello"]
  obj1 = trie()
  obj1.insert(list1)
  print("prefix : search he {}".format(obj1.prefix_search("he"))
  )
  print("prefix : search hy {}".format(obj1.prefix_search("hy"))
  )
  print("word search how {}".format(obj1.word_search("how")))
  print("word search hew {}".format(obj1.word_search("hew")))
  print("word search yellow {}".format(obj1.word_search("yellow")))
  print("autocomplete y {}".format(obj1.autocomplete("y")))

if __name__=="__main__":
  main()      
