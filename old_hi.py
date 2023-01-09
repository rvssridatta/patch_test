import argparse

#print "hello world"
#print "welcome to 2022"

def main(FLAGS):
    print("hello world")
    print("welcome to " + 2022)


if __name__ == "__main__":
    
    #Arguements
    parser = argparse.ArgumentParser()


    parser.add_argument('-i',
                        '--intel',
                        default=False,
                        help="use intel accelerated technologies")

    FLAGS = parser.parse_args()
    main(FLAGS)