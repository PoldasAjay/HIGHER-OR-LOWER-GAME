import random 
logo=""" __ __  ____   ____  __ __    ___  ____        ___   ____       _       ___   __    __    ___  ____  
|  |  ||    | /    ||  |  |  /  _]|    \      /   \ |    \     | |     /   \ |  |__|  |  /  _]|    \ 
|  |  | |  | |   __||  |  | /  [_ |  D  )    |     ||  D  )    | |    |     ||  |  |  | /  [_ |  D  )
|  _  | |  | |  |  ||  _  ||    _]|    /     |  O  ||    /     | |___ |  O  ||  |  |  ||    _]|    / 
|  |  | |  | |  |_ ||  |  ||   [_ |    \     |     ||    \     |     ||     ||  `  '  ||   [_ |    \ 
|  |  | |  | |     ||  |  ||     ||  .  \    |     ||  .  \    |     ||     | \      / |     ||  .  \
|__|__||____||___,_||__|__||_____||__|\_|     \___/ |__|\_|    |_____| \___/   \_/\_/  |_____||__|\_|
                                                                                                     
"""
vs="""
 _  _  ___ 
( \/ )/ __)
 \  / \__ \
  \/  (___/
"""


data=[{
'name': 'Ram gopal',
'follower_count': '202',
'description': 'content creater',
'country':'India'
},
{
'name': 'Ajay',
'follower_count':'220',
'description':'Homie',
'country':'India'  
},
{
'name':'Venky',
'follower_count':'400',
'description':'businessman',
'country':'Brazil'  
},
{
'name':'Avinash',
'follower_count':'5',
'description':'labour',
'country':'India'  
},
{
'name':'Virat',
'follower_count':'758',
'description':'cricketer',
'country':'India'  
},
{
'name':'VVS Laxman',
'follower_count':'650',
'description':'criketer',
'country':'India'  
},
{
'name':'Dhoni',
'follower_count':'7',
'description':'cricketer',
'country':'India'  
},
{
'name':'Messi',
'follower_count':'853',
'description':'Football player',
'country':'Argentina'
},
{
'name':'Ronaldo',
'follower_count':'976',
'description':'Football player',
'country':'Portugal'  
},
{
'name':'Hardik',
'follower_count':'805',
'description':'cricketer',
'country':'India'  
},
{
'name':'Rohit Sharma',
'follower_count':'820',
'description':'cricketer',
'country':'India'
},
{
'name':'KL Rahul',
'follower_count':'736',
'description':'cricketer',
'country':'India'  
},
{
'name':'vamshi',
'follower_count':'998',
'description':'cricketer',
'country':'India'
},
{
'name':'Bhuvaneshwar Kumar',
'follower_count':'739',
'description':'cricketer',
'country':'India'
},
{
'name':'Abhishek',
'follower_count':'684',
'description':'cricketer',
'country':'India'
},
{
'name':'Nithish Kumar Reddy',
'follower_count':'450',
'description':'cricketer',
'country':'India'
},
{
'name':'Siraj',
'follower_count':'587',
'description':'cricketer',
'country':'India'
},
{
'name':'Yuvaraj Singh',
'follower_count':'790',
'description':'cricketer',
'country':'India'
},
{
'name':'Kapildeb',
'follower_count':'400',
'description':'cricketer',
'country':'India'  
},
{
'name':'Sachin',
'follower_count':'600',
'description':'cricketer',
'country':'India'
},
{
'name':'Manish pandey',
'follower_count':'876',
'description':'cricketer',
'country':'India'
},
{
'name':'Sourav ganguly',
'follower_count':'876',
'description':'cricketer',
'country':'India'
},
{
'name':'Piyush chawla',
'follower_count':'423',
'description':'cricketer',
'country':'India'
},
{
'name':'Ravishasthri',
'follower_count':'632',
'description':'cricketer',
'country':'India'
},
{
'name':'sreeshanth',
'follower_count':'746',
'description':'cricketer',
'country':'India'
},
{
'name':'Krunal Pandya',
'follower_count':'598',
'description':'cricketer',
'country':'India'
},
{
'name':'Robin uthapa',
'follower_count':'763',
'description':'cricketer',
'country':'India'
},
{
'name':'Kuldeep yadav',
'follower_count':'538',
'description':'cricketer',
'country':'India'
},
{
'name':'Bumrah',
'follower_count':'869',
'description':'cricketer',
'country':'India'
},
{
'name':'Tilak Varma',
'follower_count':'762',
'description':'cricketer',
'country':'India'
},]





def format_data(account):
    account_name=account["name"]
    account_descr=account["description"]
    account_location=account["country"]
    return f"{account_name},a {account_descr},from {account_location}"

def check_answer(user_guess,a_followers,b_followers):
    """Take a user guess and the follower count and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print
score=0
game_should_continue = True

account_a=random.choice(data)
account_b=random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

while game_should_continue:
    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")

    guess=input("Who has more followers? Type 'A' or 'B':").lower()

    a_follower_count =account_a["follower_count"]
    b_follower_count =account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score+=1
        print(f"✅You're right Current score {score} ")
        if a_follower_count > b_follower_count:
            account_a=account_a
            account_b=random.choice(data)
        else:
            account_a=account_b
            account_b=random.choice(data)
            while account_a==account_b:
                account_b=random.choice(data)
    else:
        print(f"❌Sorry, that's Wrong. Final score: {score}")
        game_should_continue = False