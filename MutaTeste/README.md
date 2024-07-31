# mutatest
Teste para disciplina de teste

Na pasta raiz do "MutaTeste" dar:


````
python -m venv venv
source venv/bin/activate
pip install mutatest
`````

Na pasta "teste"
`````
mutatest --src . --testcmds "python -m unittest discover" -n 1

mutatest

--src .
        
--testcmds "python -m unittest discover"

-n 1
`````
    
  
# OBS:
 No MAIN, comentei para rodar o teste com o pytest ex: "mutatest --src . --testcmds "python -m unittest discover" -n 1".  

 Mas para excecutar com unittest descomente ex: "python test.py"