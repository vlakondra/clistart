import os,sys

# print(__file__, os.path.dirname( os.path.abspath(__file__) ) )
# print(" == ",os.path.dirname(os.path.pardir))
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(os.path.basename(__file__))

print(os.path.split(os.path.realpath(__file__)))
# = os.path.dirname + os.path.basename

sys.path.append(os.path.pardir)  #('/home/vkondra/MyDevs/clistart')

print(sys.path)


from clistart import __app_name__, cli
print(__app_name__)
def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()
