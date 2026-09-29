import random

def total(hand):
   
    t = sum(min(c, 10) if c > 1 else 11 for c in hand)
    aces = hand.count(1)
   
    while t > 21 and aces:
        t -= 10
        aces -= 1
    return t

def show(hand):
    
    names = {1: "A", 11: "J", 12: "Q", 13: "K"}
    return " ".join(names.get(c, str(c)) for c in hand)

def draw():
   
    return random.randint(1, 13)

chips = 500

while chips > 0:
    bet = input(f"Chips: {chips}. Bet (or q to quit): ")
    if bet == "q":
        break
    if not bet.isdigit() or not 1 <= int(bet) <= chips:
        print("Invalid bet.")
        continue
    bet = int(bet)


    player = [draw(), draw()]
    dealer = [draw(), draw()]

    
    while total(player) < 21:
        print(f"Your hand: {show(player)} = {total(player)} | Dealer shows: {show([dealer[1]])}")
        choice = input("(h)it or (s)tand? ")
        if choice == "h":
            player.append(draw())
        else:
            break

    
    if total(player) > 21:
        print(f"Bust with {total(player)}! You lose {bet}.")
        chips -= bet
        continue

    
    while total(dealer) < 17:
        dealer.append(draw())

  
    p, d = total(player), total(dealer)
    print(f"You: {show(player)} = {p} | Dealer: {show(dealer)} = {d}")
    
    if d > 21 or p > d:
        print(f"You win {bet}!")
        chips += bet
    elif p < d:
        print(f"You lose {bet}.")
        chips -= bet
    else:
        print("Push.")

print(f"You leave with {chips} chips.")
