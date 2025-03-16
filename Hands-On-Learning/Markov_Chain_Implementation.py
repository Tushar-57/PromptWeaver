# Language Model -> Takes a prompt and gives the next word, just like the keyboards

import random
from collections import defaultdict
from string import punctuation

# Maps tokens to list of possiblilites
graph = {"new": ["every", "every", "everyday", "each"], "every": ["day","day", "single"], "single":["day","time"]}

tokens = ["I", "try", "to", "learn", "something", "new", "every", "day"]

graphToken = defaultdict(list)
# graphToken["word"].append("hi") 
print(graphToken["word"]) #Empty list 

# for i, token in enumerate(tokens):
#     print(i, token)


# print(random.choice(tokens))
# print(random.choice(tokens))
# print(random.choice(tokens)) 


#Next File


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    #basic preprocessing
    def _tokenize(self, text):
        return [
        word for word in text.translate(str.maketrans("", "", punctuation + "1234567890"))
        .replace("\n", " ")
        .split(" ")
        if word  # This removes empty strings
    ]
    
    def train(self, text):
        tokens = self._tokenize(text)   
        for i, token in enumerate(tokens):
            if len(tokens)-1 == i:
                break
            self.graph[token].append(tokens[i+1])


    def generate(self, prompt, length=10):
        current = self._tokenize(prompt)[-1]
        output = prompt

        for i in range(length):
            options = self.graph.get(current, [])
            if not options:
                continue
            current = random.choice(options)
            output += f" {current}"
        return output

text = """

Andrey Markov was born on 14 June 1856 in Russia. He attended the St. Petersburg Grammar School, where some teachers saw him as a rebellious student. In his academics he performed poorly in most subjects other than mathematics. Later in life he attended Saint Petersburg Imperial University (now Saint Petersburg State University). Among his teachers were Yulian Sokhotski (differential calculus, higher algebra), Konstantin Posse (analytic geometry), Yegor Zolotarev (integral calculus), Pafnuty Chebyshev (number theory and probability theory), Aleksandr Korkin (ordinary and partial differential equations), Mikhail Okatov (mechanism theory), Osip Somov (mechanics), and Nikolai Budajev (descriptive and higher geometry). He completed his studies at the university and was later asked if he would like to stay and have a career as a Mathematician. He later taught at high schools and continued his own mathematical studies. In this time he found a practical use for his mathematical skills. He figured out that he could use chains to model the alliteration of vowels and consonants in Russian literature. He also contributed to many other mathematical aspects in his time. He died at age 66 on 20 July 1922.
Torvalds was born in Helsinki, Finland, the son of journalists Anna and Nils Torvalds,[7] the grandson of statistician Leo Törnqvist and of poet Ole Torvalds, and the great-grandson of journalist and soldier Toivo Karanko. His parents were campus radicals at the University of Helsinki in the 1960s. His family belongs to the Swedish-speaking minority in Finland. He was named after Linus Pauling, the Nobel Prize-winning American chemist, although in the book Rebel Code: Linux and the Open Source Revolution, he is quoted as saying, "I think I was named equally for Linus the Peanuts cartoon character", noting that this made him "half Nobel Prize-winning chemist and half blanket-carrying cartoon character".[8]

Torvalds attended the University of Helsinki from 1988 to 1996,[9] graduating with a master's degree in computer science from the NODES research group.[10] His academic career was interrupted after his first year of study when he joined the Finnish Navy Nyland Brigade in the summer of 1989, selecting the 11-month officer training program to fulfill the mandatory military service of Finland. He gained the rank of second lieutenant, with the role of an artillery observer.[11] He bought computer science professor Andrew Tanenbaum's book Operating Systems: Design and Implementation, in which Tanenbaum describes MINIX, an educational stripped-down version of Unix. In 1990, Torvalds resumed his university studies, and was exposed to Unix for the first time in the form of a DEC MicroVAX running ULTRIX.[12] His MSc thesis was titled Linux: A Portable Operating System.[13]

His interest in computers began with a VIC-20[14] at the age of 11 in 1981. He started programming for it in BASIC, then later by directly accessing the 6502 CPU in machine code (he did not utilize assembly language).[15] He then purchased a Sinclair QL, which he modified extensively, especially its operating system. "Because it was so hard to get software for it in Finland", he wrote his own assembler and editor "(in addition to Pac-Man graphics libraries)"[16] for the QL, and a few games.[17][18] He wrote a Pac-Man clone, Cool Man. On 5 January 1991[19] he purchased an Intel 80386-based clone of IBM PC[20] before receiving his MINIX copy, which in turn enabled him to begin work on Linux.

Linux
Main article: History of Linux
The first Linux prototypes were publicly released in late 1991.[8][21] Version 1.0 was released on 14 March 1994.[22]

Torvalds first encountered the GNU Project in 1991 when another Swedish-speaking computer science student, Lars Wirzenius, took him to the University of Technology to listen to free software guru Richard Stallman's speech.[citation needed] Torvalds used Stallman's GNU General Public License version 2 (GPLv2) for his Linux kernel.

After a visit to Transmeta in late 1996,[23] Torvalds accepted a position at the company in California, where he worked from February 1997 to June 2003. He then moved to the Open Source Development Labs, which has since merged with the Free Standards Group to become the Linux Foundation, under whose auspices he continues to work. In June 2004, Torvalds and his family moved to Dunthorpe, Oregon[24] to be closer to the OSDL's headquarters in Beaverton.

From 1997 to 1999, he was involved in 86open, helping select the standard binary format for Linux and Unix. In 1999, he was named by the MIT Technology Review TR100 as one of the world's top 100 innovators under age 35.[25]

In 1999, Red Hat and VA Linux, both leading developers of Linux-based software, presented Torvalds with stock options in gratitude for his creation.[26] That year both companies went public and Torvalds's share value briefly shot up to about US$20 million.[27][28]

His personal mascot is a penguin nicknamed Tux,[29] which has been widely adopted by the Linux community as the Linux kernel's mascot.[30]

Although Torvalds believes "open source is the only right way to do software", he also has said that he uses the "best tool for the job", even if that includes proprietary software.[31] He was criticized for his use and alleged advocacy of the proprietary BitKeeper software for version control in the Linux kernel. He subsequently wrote a free-software replacement for it called Git.

In 2008, Torvalds stated that he used the Fedora Linux distribution because it had fairly good support for the PowerPC processor architecture, which he favored at the time.[32] He confirmed this in a 2012 interview.[33] He has also posted updates about his choice of desktop environment, often in response to perceived feature regressions.

The Linux Foundation currently sponsors Torvalds so he can work full-time on improving Linux.[34]

Torvalds is known for vocally disagreeing with other developers on the Linux kernel mailing list.[35] Calling himself a "really unpleasant person", he explained, "I'd like to be a nice person and curse less and encourage people to grow rather than telling them they are idiots. I'm sorry—I tried, it's just not in me."[36][37] His attitude, which he considers necessary for making his points clear, has drawn criticism from Intel programmer Sage Sharp and systemd developer Lennart Poettering, among others.[38][failed verification][39]

On Sunday, 16 September 2018, the Linux kernel Code of Conflict was suddenly replaced by a new Code of Conduct based on the Contributor Covenant. Shortly thereafter, in the release notes for Linux 4.19-rc4, Torvalds apologized for his behavior, calling his personal attacks of the past "unprofessional and uncalled for" and announced a period of "time off" to "get some assistance on how to understand people's emotions and respond appropriately". It soon transpired that these events followed The New Yorker approaching Torvalds with a series of questions critical of his conduct.[40][41][42] Following the release of Linux 4.19 on 22 October 2018, Torvalds returned to maintaining the kernel.[43]
"""

marObj = MarkovChain()
# tokenText = marObj._tokenize(text)
# print(tokenText)
marObj = MarkovChain()
marObj.train(text)
graphObj = marObj.graph  # Check if words are stored correctly
print(marObj.generate("My name is Tushar Sharma and I ", 5))  # Test generation
# newObj = marObj.generate(text)
# print(newObj)


#Visualizing the created graph

# !pip install networkxpip
# import networkx as nx
# import matplotlib.pyplot as plt

# # Your map


# # Create a directed graph
# G = nx.DiGraph()

# # Add edges
# for key, values in graphObj.items():
#     for value in values:
#         G.add_edge(key, value)

# # Draw the graph
# plt.figure(figsize=(12, 8))
# pos = nx.spring_layout(G, seed=42)  # Layout for better visualization
# nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10, font_weight="bold")
# plt.title("Graph Visualization of Word Map")
# plt.show()
