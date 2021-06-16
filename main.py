from game_env import Main

mode = 'fit'
# or test
if __name__ == '__main__':
    game = Main(1280, 720, 60)
    game.run()
