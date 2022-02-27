import pyperclip as pc

import pygame

pygame.init()

timestamp = {"Act I": "00H:00m:49s",
             "Alexander Hamilton": "00H:01m:06s",
             "Aaron Burr, Sir": "00H:05m:08s",
             "My Shot": "00H:07m:42s",
             "The Story Of Tonight": "00H:13m:44s",
             "The Schuyler Sisters": "00H:15m:12s",
             "Farmer Refuted": "00H:18m:24s",
             "You'll Be Back": "00H:20m:14s",
             "Right-hand Man": "00H:24m:11s",
             "A Winter's Ball": "00H:29m:34s",
             "Helpless": "00H:30m:43s",
             "Satisfied": "00H:34m:59s",
             "The Story of Tonight (Reprise)": "00H:40m:39s",
             "Wait For It": "00H:42m:36s",
             "Stay Alive": "00H:45m:57s",
             "Ten Duel Commandments": "00H:48m:37s",
             "Meet Me Inside": "00H:50m:24s",
             "That Would Be Enough": "00H:51m:53s",
             "Guns and Ships": "00H:54m:48s",
             "History Has Its Eyes On You": "00H:57m:01s",
             "Yorktown (The World Turned Upside Down)": "00H:58m:44s",
             "What Comes Next": "01H:03m:13s",
             "Dear Theodosia": "01H:05m:01s",
             "Non-Stop": "01H:08m:59s",
             "Act II:-": "1H:16m:30s",
             "What'd I Miss": "01H:16m:35s",
             "Cabinet Battle #1": "01H:20m:39s",
             "Take A Break": "01H:24m:30s",
             "Say No To This": "01H:29m:21s",
             "The Room Where It Happens": "01H:33m:30s",
             "Schuyler Defeated": "01H:39m:02s",
             "Cabinet Battle #2": "01H:40m:05s",
             "Washington On Your Side": "01H:42m:29s",
             "One Last Time": "01H:45m:31s",
             "I Know Him": "01H:50m:55s",
             "The Adams Administration": "01H:52m:53s",
             "We Know": "01H:53m:49s",
             "Hurricane": "01H:56m:17s",
             "The Reynolds Pamphlet": "01H:58m:48s",
             "Burn": "02H:00m:57s",
             "Blow Us All Away": "02H:04m:52s",
             "Stay Alive (Reprise)": "02H:07m:48s",
             "It's Quiet Uptown": "02H:09m:52s",
             "Election of 1800": "02H:14m:31s",
             "Your Obedient Servant": "02H:18m:33s",
             "Best of Wives and Best of Women": "02H:21m:03s",
             "The World Was Wide Enough": "02H:21m:54s",
             "Who Lives, Who Dies, Who Tells Your Story": "02H:27m:12s",
             "Credits": "02H:32m:05s"}

timestamp_keys = ['Act I', 'Alexander Hamilton', 'Aaron Burr, Sir', 'My Shot', 'The Story Of Tonight',
                  'The Schuyler Sisters', 'Farmer Refuted', "You'll Be Back", 'Right-hand Man', "A Winter's Ball",
                  'Helpless', 'Satisfied', 'The Story of Tonight (Reprise)', 'Wait For It', 'Stay Alive',
                  'Ten Duel Commandments', 'Meet Me Inside', 'That Would Be Enough', 'Guns and Ships',
                  'History Has Its Eyes On You', 'Yorktown (The World Turned Upside Down)', 'What Comes Next',
                  'Dear Theodosia', 'Non-Stop', 'Act II:-', "What'd I Miss", 'Cabinet Battle #1', 'Take A Break',
                  'Say No To This', 'The Room Where It Happens', 'Schuyler Defeated', 'Cabinet Battle #2',
                  'Washington On Your Side', 'One Last Time', 'I Know Him', 'The Adams Administration', 'We Know',
                  'Hurricane', 'The Reynolds Pamphlet', 'Burn', 'Blow Us All Away', 'Stay Alive (Reprise)',
                  "It's Quiet Uptown", 'Election of 1800', 'Your Obedient Servant', 'Best of Wives and Best of Women',
                  'The World Was Wide Enough', 'Who Lives, Who Dies, Who Tells Your Story', 'Credits']

timestamp_values = ['00H:00m:49s', '00H:01m:06s', '00H:05m:08s', '00H:07m:42s', '00H:13m:44s', '00H:15m:12s',
                    '00H:18m:24s', '00H:20m:14s', '00H:24m:11s', '00H:29m:34s', '00H:30m:43s', '00H:34m:59s',
                    '00H:40m:39s', '00H:42m:36s', '00H:45m:57s', '00H:48m:37s', '00H:50m:24s', '00H:51m:53s',
                    '00H:54m:48s', '00H:57m:01s', '00H:58m:44s', '01H:03m:13s', '01H:05m:01s', '01H:08m:59s',
                    '1H:16m:30s', '01H:16m:35s', '01H:20m:39s', '01H:24m:30s', '01H:29m:21s', '01H:33m:30s',
                    '01H:39m:02s', '01H:40m:05s', '01H:42m:29s', '01H:45m:31s', '01H:50m:55s', '01H:52m:53s',
                    '01H:53m:49s', '01H:56m:17s', '01H:58m:48s', '02H:00m:57s', '02H:04m:52s', '02H:07m:48s',
                    '02H:09m:52s', '02H:14m:31s', '02H:18m:33s', '02H:21m:03s', '02H:21m:54s', '02H:27m:12s',
                    '02H:32m:05s']

screen = pygame.display.set_mode((800, 600))

a = 0
b = 0
c = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            b += 1
            if event.key == pygame.K_SPACE:
                if b % 2 == 0:
                    pc.copy(timestamp_keys[a])
                    print(timestamp_keys[a])
                    a += 1
                if b % 2 != 0:
                    pc.copy(timestamp_values[c])
                    print(timestamp_values[c])
                    c += 1

