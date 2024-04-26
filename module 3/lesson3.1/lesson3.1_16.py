comb = input()
comb2 = input()
black = 'a1a3a5a7a9b2b4b6b8c1c3c5c7c9d2d4d6d8e1e3e5e7e9f2f4f6f8g1g3g5g7g9h2h4h6h8'
white = 'a2a4a6a8b1b3b5b7b9c2c4c6c8d1d3d5d7d9e2e4e6e8f1f3f5f7f9g2g4g6g8h1h3h5h7h9'
if (comb in black and comb2 in black) or (comb in white and comb2 in white):
    print('YES')
else:
    print('NO')
