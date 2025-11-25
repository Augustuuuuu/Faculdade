# enigma3.py
# Enigma simples com 3 rotores, refletor e plugboard.
# Trabalha apenas com letras A-Z. Letras acentuadas devem ser normalizadas manualmente.

import string
import unicodedata

ALFABETO = string.ascii_uppercase  # 'A'..'Z'
A_IDX = {c: i for i, c in enumerate(ALFABETO)}

def remover_acentos_e_maiusculas(texto: str) -> str:
    # Remove acentos e transforma em maiúsculas
    nfkd = unicodedata.normalize('NFKD', texto)
    sem_acento = ''.join([c for c in nfkd if not unicodedata.combining(c)])
    return sem_acento.upper()

class Rotor:
    def __init__(self, nome, fiação, notch, posicao='A', anel=1):
        """
        fiação: string 26 letras que mapeia entrada->saída no sentido A..Z
        notch: letras onde o rotor provoca avanço do rotor à esquerda (ex: 'Q')
        posicao: letra inicial (A..Z)
        anel: ring setting (1..26) como na máquina física
        """
        assert len(fiação) == 26
        self.nome = nome
        self.fiação = fiação
        self.notch = notch
        self.pos = A_IDX[posicao.upper()]
        self.anel = anel - 1  # converter para 0-based

        # cria fiação inversa para mapeamento de retorno
        self.fiação_inv = [''] * 26
        for i, ch in enumerate(self.fiação):
            self.fiação_inv[A_IDX[ch]] = ALFABETO[i]
        self.fiação_inv = ''.join(self.fiação_inv)

    def step(self):
        self.pos = (self.pos + 1) % 26

    def is_at_notch(self) -> bool:
        # verifica se a letra visível está na posição de notch
        letra_visivel = ALFABETO[self.pos]
        return letra_visivel in self.notch

    def forward(self, c_idx: int) -> int:
        """Mapeamento no sentido do teclado -> refletor"""
        # considerar offset de posição e ring setting
        idx = (c_idx + self.pos - self.anel) % 26
        letra_saida = self.fiação[idx]
        return (A_IDX[letra_saida] - self.pos + self.anel) % 26

    def backward(self, c_idx: int) -> int:
        """Mapeamento no sentido refletor -> teclado (retorno pelo rotor)"""
        idx = (c_idx + self.pos - self.anel) % 26
        letra_saida = self.fiação_inv[idx]
        return (A_IDX[letra_saida] - self.pos + self.anel) % 26

class Enigma:
    def __init__(self, rotores, refletor, plugboard=None):
        """
        rotores: lista de 3 instâncias Rotor na ordem [esquerdo, meio, direito]
        refletor: dicionário de mapeamento A->X, X->A etc (26 pares)
        plugboard: dict opcional com trocas (p.ex. {'A':'B','B':'A', ...})
        """
        assert len(rotores) == 3
        self.esq, self.mei, self.dir = rotores
        self.refletor = refletor
        self.plugboard = plugboard or {}

    def _passar_plugboard(self, ch):
        return self.plugboard.get(ch, ch)

    def _passar_refletor(self, idx):
        letra = ALFABETO[idx]
        letra_r = self.refletor[letra]
        return A_IDX[letra_r]

    def _step_rotores(self):
        # Implementa stepping com double-stepping
        # Se o rotor do meio estiver em notch -> avançar rotor esquerdo
        if self.mei.is_at_notch():
            self.esq.step()
            self.mei.step()
        # Se rotor direito estiver em notch -> avancar rotor meio
        elif self.dir.is_at_notch():
            self.mei.step()
        # rotor direito sempre avança
        self.dir.step()

    def cifrar_char(self, ch):
        if ch not in ALFABETO:
            return ch  # mantém caracteres não A-Z

        # 1) avanço rotores
        self._step_rotores()

        # 2) plugboard in
        ch = self._passar_plugboard(ch)
        idx = A_IDX[ch]

        # 3) passagem pelos rotores (direito -> meio -> esquerdo)
        idx = self.dir.forward(idx)
        idx = self.mei.forward(idx)
        idx = self.esq.forward(idx)

        # 4) refletor
        idx = self._passar_refletor(idx)

        # 5) retorno (esquerdo -> meio -> direito), sentido inverso
        idx = self.esq.backward(idx)
        idx = self.mei.backward(idx)
        idx = self.dir.backward(idx)

        # 6) plugboard out
        letra_saida = ALFABETO[idx]
        letra_saida = self._passar_plugboard(letra_saida)

        return letra_saida

    def cifrar_texto(self, texto):
        resultado = []
        for ch in texto:
            if ch.upper() in ALFABETO:
                resultado.append(self.cifrar_char(ch.upper()))
            else:
                # mantém espaços e pontuação (ou poderia remover)
                resultado.append(ch)
        return ''.join(resultado)


# --- Exemplo de rotores e refletor padrão histórico (I, II, III e Reflector B) ---
# Fiações históricas (Wiring)
ROTOR_I   = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"; NOTCH_I = "Q"
ROTOR_II  = "AJDKSIRUXBLHWTMCQGZNPYFVOE"; NOTCH_II = "E"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"; NOTCH_III = "V"
REFLECTOR_B = {a: b for a, b in zip(ALFABETO, "YRUHQSLDPXNGOKMIEBFZCWVJAT")}  # B

# plugboard exemplo (pareamentos)
EX_PLUGBOARD = {
    # 'A': 'B', 'B': 'A',
    # 'C': 'D', 'D': 'C'
}
# - completar plugboard se desejar trocas

# Cria instâncias Rotor (nome, fiação, notch, posição inicial, ring setting)
rot_esq = Rotor("I", ROTOR_I, NOTCH_I, posicao='A', anel=1)
rot_mei = Rotor("II", ROTOR_II, NOTCH_II, posicao='A', anel=1)
rot_dir = Rotor("III", ROTOR_III, NOTCH_III, posicao='A', anel=1)

# Monta máquina
maquina = Enigma([rot_esq, rot_mei, rot_dir], REFLECTOR_B, plugboard=EX_PLUGBOARD)

# --- Função de utilidade para exemplo ---
def exemplo_uso():
    frase = "DIGITE NO QUADRO O AUGUSTO E LINDO"
    frase = remover_acentos_e_maiusculas(frase)  # transforma e remove acentos
    print("Texto limpo:", frase)

    # Ajuste posições iniciais e ring settings se quiser; aqui usamos AAA e ring=1.
    # (Caso queira definir posicoes iniciais diferentes:)
    rot_esq.pos = A_IDX['A']
    rot_mei.pos = A_IDX['A']
    rot_dir.pos = A_IDX['A']

    criptografado = maquina.cifrar_texto(frase)
    print("Criptografado:", criptografado)

    # Para descriptografar, re-crie a máquina com as mesmas configurações iniciais
    # (Enigma é simétrica: aplicar a mesma operação com mesmas posições decifra)
    # reiniciando posições:
    rot_esq.pos = A_IDX['A']
    rot_mei.pos = A_IDX['A']
    rot_dir.pos = A_IDX['A']
    decifrado = maquina.cifrar_texto(criptografado)
    print("Decifrado:", decifrado)

if __name__ == "__main__":
    exemplo_uso()
