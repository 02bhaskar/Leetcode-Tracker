# Last updated: 9/1/2026, 10:29:17 PM
1class Trie(object):
2
3	def __init__(self):
4		self.trie = {}
5
6
7	def insert(self, word):
8		t = self.trie
9		for c in word:
10			if c not in t: t[c] = {}
11			t = t[c]
12		t["-"] = True
13
14
15	def search(self, word):
16		t = self.trie
17		for c in word:
18			if c not in t: return False
19			t = t[c]
20		return "-" in t
21
22	def startsWith(self, prefix):
23		t = self.trie
24		for c in prefix:
25			if c not in t: return False
26			t = t[c]
27		return True