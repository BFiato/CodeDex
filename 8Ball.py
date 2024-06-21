rpt = 'yes'
while (rpt != 'no'):
  import random
  eightball = ['Yes - definitely.', 'It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.'  ];
  input('Question: ')
  num = random.randint(0, 8)
  print('Magic 8 Ball: ', eightball[num])
  rpt = input('Do you have another question? ')
