br = 'botafogo', 'palmeiras', 'flamengo', 'atlético-mg', 'fluminense', 'grêmio', 'athletico-pr', 'são paulo', 'cruzeiro', 'internacional', 'fortaleza', 'red bull bragantino', 'santos', 'cuiabá', 'bahia', 'corinthians', 'goiás', 'américa-mg', 'vasco', 'coritiba'
print(f'''
-----------------------------------------
              BRASILEIRÃO
-----------------------------------------
[A] os cinco primeiros colocados são:
{br[0:5]}
-----------------------------------------
[B] os quatro últimos colocados são: 
{br[0:4]}
-----------------------------------------
[C] os times em ordem alfabética são:
{sorted(br)}
-----------------------------------------
[D] o São Paulo está na posição {br.index('são paulo')+1}
-----------------------------------------''')
