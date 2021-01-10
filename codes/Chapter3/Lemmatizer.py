# 3장 전처리 - 두 단문 처리와 둘 사이의 공통 어휘 추출
# www.enlgish-for-students.com
story1 = '''Once there lived a cat. She thought, "The lion is the strongest of all the animals. It is good to have strong friends. I shall go to the lion and make friendship with him."
She did so and the lion and the cat were friends for many, many days.
Once they went for a walk together and met an elephant. The lion began to fight with the elephant and the elephant killed him.
The cat was very sorry. "What shall I do?" she thought.
"The elephant was stronger than the lion. I shall go to the elephant and make friendship with him."
She did so and they were friends for many, many days.
Once they went for a walk and met a hunter. The hunter shot at the elephant and killed him. The cat was sorry, but she thought, "The man is stronger than the elephant, I see."
So she went up to the hunter and asked, "May I go with you?"
"All right, let us go home together," he said.
They came to the man's home. His wife met him and took his gun from him. The cat saw that and thought: "Oh, the woman is the strongest of all! She can take the hunter's gun from him, and he does not fight with her. He does not even say a word!" The man sat down at the table and the woman went to the kitchen. The cat went to the kitchen, too. She decided to stay with the woman forever. That's why you always see a cat in the kitchen at a woman's feet.
'''
story2 = '''When he was a strong young cat, he caught many mice. The mice were afraid of him then. But in time he grew old and could not catch mice any more.
One day he decided to play a trick on the mice. He lay on his back and did not move at all.
A mouse saw him and thought he was dead. She ran to her friends and said, "The cat is dead! Let us dance and play!"
And all the mice began to dance and play. They were very happy. They danced and danced round the cat and the cat did not move.
Then one of the mice jumped on the cat's head. "Look at me! Come nearer, all of you! The bad cat is dead! Let us dance on his head!" But suddenly the cat jumped up and caught the silly mouse.
The other mice ran away as quickly as they could.
Mice! Don't forget! Never believe a cat!
'''

# 특수문자 제거
story1 = story1.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!", "").replace("?", "").casefold()
story2 = story2.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!", "").replace("?", "").casefold()

# 단어 분리
story1_words = story1.split(" ")
print("첫 번째 이야기 단어 :", story1_words)
story2_words = story2.split(" ")
print("두 번째 이야기 단어 :", story2_words)

# 어휘 만들기
story1_vocab = set(story1_words)
print("첫 번째 이야기 어휘 :", story1_vocab)
story2_vocab = set(story2_words)
print("두 번째 이야기 어휘 :", story2_vocab)

# 공통 어휘 생성
common_vocab = story1_vocab & story2_vocab    # 합집합 연산 &
print("공통 어휘 :", common_vocab)
