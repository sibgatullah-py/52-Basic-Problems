
def rate(n):
    while n > 0:
        target = int(input('Target score: '))
        score = int(input('Score: '))
        balls_left = int(input('Balls left: '))
        ball_played = 300 - balls_left
        current_run_rate = (score/ball_played) * 6
        asking_run_rate = ((target - score + 1)/balls_left) * 6
        print(current_run_rate,' ',asking_run_rate)
        
        n-=1
        
rate(int(input()))