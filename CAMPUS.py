class Curso:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome
        self.codigo = codigo

    def __str__(self):
        return f"Curso(código={self.codigo}, nome={self.nome})"


class Campus:
    def __init__(self, nome: str, sigla: str):
        self.nome = nome
        self.sigla = sigla
        self.cursos = []  # lista de cursos

    def adicionar_curso(self, curso: Curso):
        for c in self.cursos:
            if c.codigo == curso.codigo:
                print(f"Já existe curso com código {curso.codigo} no campus {self.sigla}")
                return False
        self.cursos.append(curso)
        return True

    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado neste campus.")
        for i, curso in enumerate(self.cursos):
            print(f"{i + 1}. {curso}")

    def buscar_curso_por_codigo(self, codigo: str):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def remover_curso(self, codigo: str):
        curso = self.buscar_curso_por_codigo(codigo)
        if curso:
            self.cursos.remove(curso)
            return True
        return False

    def atualizar_curso(self, codigo: str, novo_nome: str = None, novo_codigo: str = None):
        curso = self.buscar_curso_por_codigo(codigo)
        if not curso:
            return False
        if novo_nome:
            curso.nome = novo_nome
        if novo_codigo:
            # verificar se não existe outro curso com esse novo código
            if any(c.codigo == novo_codigo for c in self.cursos if c is not curso):
                print("Já existe outro curso com esse novo código.")
                return False
            curso.codigo = novo_codigo
        return True

    def __str__(self):
        return f"Campus(sigla={self.sigla}, nome={self.nome}, total de cursos={len(self.cursos)})"


class SistemaUFC:
    def __init__(self):
        self.campuses = []  # lista de Campus

    def adicionar_campus(self, campus: Campus):
        # checa duplicado por sigla
        for c in self.campuses:
            if c.sigla == campus.sigla:
                print(f"Já existe campus com sigla {campus.sigla}")
                return False
        self.campuses.append(campus)
        return True

    def listar_campuses(self):
        if not self.campuses:
            print("Nenhum campus cadastrado.")
        for i, campus in enumerate(self.campuses):
            print(f"{i + 1}. {campus}")

    def buscar_campus_por_sigla(self, sigla: str):
        for campus in self.campuses:
            if campus.sigla.lower() == sigla.lower():
                return campus
        return None

    def remover_campus(self, sigla: str):
        campus = self.buscar_campus_por_sigla(sigla)
        if campus:
            self.campuses.remove(campus)
            return True
        return False

    def atualizar_campus(self, sigla: str, novo_nome: str = None, nova_sigla: str = None):
        campus = self.buscar_campus_por_sigla(sigla)
        if not campus:
            return False
        if novo_nome:
            campus.nome = novo_nome
        if nova_sigla:
            if any(c.sigla == nova_sigla for c in self.campuses if c is not campus):
                print("Já existe outro campus com essa nova sigla.")
                return False
            campus.sigla = nova_sigla
        return True

    def menu(self):
        while True:
            print("\n=== Sistema UFC ===")
            print("1. Gerenciar Câmpus")
            print("2. Gerenciar Cursos de um Campus")
            print("3. Sair")
            opc = input("Escolha uma opção: ")

            if opc == "1":
                self.menu_campuses()
            elif opc == "2":
                self.menu_cursos()
            elif opc == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def menu_campuses(self):
        while True:
            print("\n--- Menu Câmpus ---")
            print("1. Criar campus")
            print("2. Listar câmpus")
            print("3. Atualizar campus")
            print("4. Remover campus")
            print("5. Voltar")
            opc = input("Escolha uma opção: ")

            if opc == "1":
                nome = input("Nome do campus: ")
                sigla = input("Sigla do campus: ")
                campus = Campus(nome, sigla)
                ok = self.adicionar_campus(campus)
                if ok:
                    print("Campus criado com sucesso.")
            elif opc == "2":
                self.listar_campuses()
            elif opc == "3":
                sigla = input("Sigla do campus a atualizar: ")
                campus = self.buscar_campus_por_sigla(sigla)
                if not campus:
                    print("Campus não encontrado.")
                else:
                    novo_nome = input("Novo nome (deixe vazio para não mudar): ")
                    nova_sigla = input("Nova sigla (deixe vazio para não mudar): ")
                    sucesso = self.atualizar_campus(sigla, novo_nome or None, nova_sigla or None)
                    if sucesso:
                        print("Campus atualizado com sucesso.")
                    else:
                        print("Falha ao atualizar campus.")
            elif opc == "4":
                sigla = input("Sigla do campus a remover: ")
                sucesso = self.remover_campus(sigla)
                if sucesso:
                    print("Campus removido.")
                else:
                    print("Campus não encontrado.")
            elif opc == "5":
                break
            else:
                print("Opção inválida.")

    def menu_cursos(self):
        sigla = input("Digite a sigla do campus para gerenciar cursos: ")
        campus = self.buscar_campus_por_sigla(sigla)
        if not campus:
            print("Campus não encontrado.")
            return

        while True:
            print(f"\n--- Menu Cursos do Campus {campus.sigla} ---")
            print("1. Adicionar curso")
            print("2. Listar cursos")
            print("3. Atualizar curso")
            print("4. Remover curso")
            print("5. Voltar")
            opc = input("Escolha uma opção: ")

            if opc == "1":
                nome = input("Nome do curso: ")
                codigo = input("Código do curso: ")
                curso = Curso(nome, codigo)
                ok = campus.adicionar_curso(curso)
                if ok:
                    print("Curso adicionado.")
            elif opc == "2":
                campus.listar_cursos()
            elif opc == "3":
                codigo = input("Código do curso a atualizar: ")
                curso = campus.buscar_curso_por_codigo(codigo)
                if not curso:
                    print("Curso não encontrado.")
                else:
                    novo_nome = input("Novo nome (deixe vazio para não mudar): ")
                    novo_codigo = input("Novo código (deixe vazio para não mudar): ")
                    sucesso = campus.atualizar_curso(codigo, novo_nome or None, novo_codigo or None)
                    if sucesso:
                        print("Curso atualizado.")
                    else:
                        print("Falha ao atualizar curso.")
            elif opc == "4":
                codigo = input("Código do curso a remover: ")
                sucesso = campus.remover_curso(codigo)
                if sucesso:
                    print("Curso removido.")
                else:
                    print("Curso não encontrado.")
            elif opc == "5":
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    sistema = SistemaUFC()
    sistema.menu()
