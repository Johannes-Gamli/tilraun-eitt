#geyma tölu sem heitir biggest sem byrjar sem mínus einn
#nota lykkju þangað til að inntak er stærra eða jafnt núll
#lykkja athugar hvort inntak sé stærra en biggest og ef svo er setur biggest sem inntak
#þegar lykkja hættir prenta biggest ef biggest er eitthvað annað en mínus einn
biggest=-1
in0=int(input("Input a number: "))
while in0<0:
    if biggest<in0:
        biggest=in0
    in0=int(input("Input a number: "))
else:
    if(biggest!=-1):
        print(biggest)
