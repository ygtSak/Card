#オブジェクト指向_まとめ
#ゲーム「Card」

class Card:
  """
クラス[Card]:ゲームで使用するカード情報について操作するクラス
[変数]
  VALUES(list):トランプのカードの値（２〜１０、エース、ジャック、クイーン、キング）を管理するリスト型の変数
  SUITS(list):トランプの柄（スペード、ハート、ダイアモンド、クラブ）を管理するリスト型の変数

[注釈]
  リストの並び順がカードの強弱を決定します。
  トランプの値は２が最も弱く、逆に最も強くなるのはキングではなくエースになります。
  トランプの柄は初期値の並び順で強弱が決まっています。
  
[ゲームルール]
  トランプは、値と柄がセットになった５２枚のカードを使用します。
  トランプのカードを比較する際は値を優先的に比較し、もし同じ場合なら柄を比較して勝敗を決めます。

  """

  VALUES = [None,None,
            2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

  SUITS = ["spades","hearts","diamonds","clubs"]

  def __init__(self,v,s):
    self.value = v
    self.suit = s   

  def __lt__(self,c2):
    """
比較演算子「未満(<)」を使えるようにするための特殊メソッド
    """
    if self.value < c2.value:
      return True
    if self.value == c2.value:
      if self.suit < c2.suit:
        return True
      else:
        return False
    return False

  def __gt__(self,c2):
    """
比較演算子「超過(>)」を使えるようにするための特殊メソッド
    """
    if self.value > c2.value:
      return True
    if self.value == c2.value:
      if self.suit > self.suit:
        return True
      else:
        return False
    return False

  def __repr__(self):
    return str(self.VALUES[self.value]) + " of " + str(self.SUITS[self.suit])


from random import shuffle

class Deck:
  """
クラス[Deck]:ゲームで使用するカードの情報を一つのデッキにまとめて、編集・管理するクラスオブジェクト
  """
  def __init__(self):
    self.cards = []

    for i in range(2,15):
      for j in range(4):
        self.cards.append(Card(i,j))
    shuffle(self.cards)

  def rm_card(self):
    if len(self.cards) != 0:
      return self.cards.pop()

class Player:
    def __init__(self,name):
      self.wins = 0
      self.card = None
      self.name = name

class Game:
  """
クラス[Game]:ゲームを遊ぶためのクラスオブジェクト。プレイヤーの名前設定から、ゲームの勝敗まで制御する。
  """
  def __init__(self):
    name1 = input("プレイヤー１の名前")
    name2 = input("プレイヤー２の名前")
    self.deck = Deck()
    self.p1 = Player(name1)
    self.p2 = Player(name2)

  def wins(self,winner):
    print("このラウンドは{}が勝ちました！".format(winner))

  def draw(self,p1n,p1c,p2n,p2c):
    print("{}は{}、{}は{}を引きました。".format(p1n,p1c,p2n,p2c))

  def winner(self,p1,p2):
    if p1.wins > p2.wins:
      return p1.name
    elif p1.wins < p2.wins:
      return p2.name
    else:
      return "引き分け"

  def play_game(self):
    cards = self.deck.cards
    print("戦争を始めます")

    while len(cards) >= 2:
      m = "q->終了、それ以外->プレイ"
      response = input(m)

      if response == 'q':
        break
      
      p1c = self.deck.rm_card()
      p2c = self.deck.rm_card()
      p1n = self.p1.name
      p2n = self.p2.name
      self.draw(p1n,p1c,p2n,p2c)

      if p1c > p2c:
        self.p1.wins += 1
        self.wins(self.p1.name)
      else:
        self.p2.wins += 1
        self.wins(self.p2.name)
    win = self.winner(self.p1,self.p2)


#-------------------#


def test():
  card1 = Card(2,1)
  print(card1)
  card2 = Card(2,3)
  print(card2)

  print(card1 < card2)

  deck = Deck()
  i=1
  for card in deck.cards:
    print("{}){}".format(i,card))
    i+=1

def main():
  game = Game()
  game.play_game()

main()