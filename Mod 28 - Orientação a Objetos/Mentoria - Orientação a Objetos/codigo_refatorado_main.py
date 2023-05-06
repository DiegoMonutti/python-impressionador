from codigo_refatorado_classe import MeuRobo

robo = MeuRobo(3)
robo.abrir_programa('chrome')
robo.digitar_aguardar('https://www.hashtagtreinamentos.com/blog')
robo.clicar(x=1157, y=503)
robo.digitar_aguardar('classe')
robo.clicar(x=614, y=535)
robo.aguardar()
robo.clicar(x=303, y=646, botao='right')