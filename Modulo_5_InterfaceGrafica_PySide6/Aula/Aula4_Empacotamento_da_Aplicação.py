"""
Empacotamento de aplicações Python
pip install PyInstaller
Documentação: https://pyinstaller.org/en/stable/
Dicas de Empacotamento: https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/

Para iniciar o empacotamento precisamos sempre saber o caminho correto dos arquivos, tendo isso vamos seguir.

Nomeando a aplicação: pyinstaller --name"Nome que quiser para a aplicação"
Comando para evitar mensagem de confirmação: --noconfirm
Para ter apenas um arquivos adicionamos: --onefile
Adicionar arquivos opcionais como imagens nesse único arquivo: --add-data="O caminho do arquivo;nome da pasta do novo arquivo"
No mac ou linux o comando é o mesmo porém é trocado o ; por : : --add-data="O caminho do arquivo:nome da pasta do novo arquivo"
Adicionar o ícone da aplicação: --icon='caminho do icone'
Não abrir o console: --noconsole
Receber registros de log de alguma coisa: --log-level=o tipo de log(WARN) log de alertas
Definir um local para onde ficará o executável: --distpath="Caminho que desejar"
Definir local dos arquivos de build, que montam o sistema: --workpath="Caminho que desejar"
E por fim coloca o caminho do arquivo principal de execução da aplicação

pyinstaller --name="Calculadora" --noconfirm --onefile --add-data='..\\Modulo_5_InterfaceGrafica_PySide6\\Calculadora\\img;img\\
' --icon='..\\Modulo_5_InterfaceGrafica_PySide6\\Calculadora\\img\\calculadora.png' --noconsole --clean --log-level=WARN
--distpath="C:\\Users\\HSVP\\Desktop"
--workpath="C:\\Users\\HSVP\\Documents\\CalculadoraPython" Modulo_5_InterfaceGrafica_PySide6\\Calculadora\\main.py
"""
