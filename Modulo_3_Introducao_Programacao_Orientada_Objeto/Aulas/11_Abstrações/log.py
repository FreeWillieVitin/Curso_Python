"""
Abstração
"""
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg): # Método Abstrato
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg): # Método Concreto
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a', encoding='utf8') as file:
            file.write(msg_formatada)
            file.write('\n')
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('Qualquer coisa')
    l.log_success('Deu certo')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Deu certo')
    print(LOG_FILE)