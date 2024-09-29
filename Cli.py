import cmd

class Cli(cmd.Cmd):
    prompt = ">>>"
    intro = "Bem Vindo a Lista de Tarefas. Para ajuda digite 'help'."

    def do_ola(self, line):
        print("Olá")
    def do_sair(self, line):
        return True

if __name__ == "__main__":
    Cli().cmdloop()