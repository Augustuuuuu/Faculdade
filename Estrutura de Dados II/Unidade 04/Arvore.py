class Node:
  """
  Classe para representar um nó na árvore.

  Esta classe define a estrutura básica de um nó na árvore. Cada nó possui um valor
  e dois ponteiros, um para o filho à esquerda e outro para o filho à direita.

  Atributos:
      value: O valor armazenado no nó.
      left: O ponteiro para o filho à esquerda.
      right: O ponteiro para o filho à direita.
  """
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree:
  """
  Classe para representar uma árvore binária.

  Esta classe gerencia a árvore binária, incluindo operações de inserção, busca,
  remoção e travessias.

  Atributo:
      root: O nó raiz da árvore.
  """
  def __init__(self):
    self.root = None

  def insert(self, value):
    """
    Insere um novo valor na árvore.

    Esta função insere um novo valor na árvore binária utilizando uma pesquisa
    recursiva. O valor é inserido na posição correta de acordo com a ordem
    crescente.

    Argumentos:
        value: O valor a ser inserido na árvore.

    Retorno:
        Nenhum.
    """
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      return
    parent = None
    current = self.root
    while current is not None:
      parent = current
      if value < current.value:
        current = current.left
      else:
        current = current.right
    if value < parent.value:
      parent.left = new_node
    else:
      parent.right = new_node

  def search(self, value):
    """
    Busca um valor na árvore.

    Esta função verifica se um determinado valor existe na árvore binária.
    A pesquisa é realizada utilizando uma travessia recursiva em pré-ordem.

    Argumentos:
        value: O valor a ser buscado na árvore.

    Retorno:
        True se o valor for encontrado, False caso contrário.
    """
    current = self.root
    while current is not None:
      if current.value == value:
        return True
      elif value < current.value:
        current = current.left
      else:
        current = current.right
    return False

  def remove(self, value):
    """
    Remove um valor da árvore.

    Esta função remove um valor específico da árvore binária. A remoção é feita
    de maneira recursiva, considerando os diferentes casos possíveis (nó folha,
    nó com um filho e nó com dois filhos).

    Argumentos:
        value: O valor a ser removido da árvore.

    Retorno:
        Nenhum.
    """
    parent = None
    current = self.root
    while current is not None:
      if current.value == value:
        break
      elif value < current.value:
        parent = current
        current = current.left
      else:
        parent = current
        current = current.right
    if current is None:
      return
    if current.left is None and current.right is None:
      # Nó folha
      if parent is None:
        self.root = None
      elif value < parent.value:
        parent.left = None
      else:
        parent.right = None
    elif current.left is None:
      # Nó com um filho à direita
      if parent is None:
        self.root = current.right
      elif value < parent.value:
        parent.left = current.right
      else:
        parent.right = current.right
    elif current.right is None:
      # Nó com um filho à esquerda
      if parent is None:
        self.root = current.left
      elif value < parent.value:
        parent.left = current.left
      else:
        parent.right = current.left
    else:
      # Nó com dois filhos
      successor = self.get_min_node(current.right)
      self.remove(successor.value)
      successor.left = current.left
      successor.right = current.right
      if parent is None:
        self.root = successor

  def get_min_node(self, node):
    """
    Obtém o nó mínimo de uma subárvore.

    Esta função auxiliar encontra o nó com o menor valor em uma subárvore
    especificada. A busca é feita de forma recursiva, sempre seguindo o filho
    à esquerda até encontrar um nó que não possui filho à esquerda.

    Argumentos:
        node: O nó raiz da subárvore na qual se deseja encontrar o menor valor.

    Retorno:
        O nó com o menor valor na subárvore.
    """
    while node.left is not None:
      node = node.left
    return node

  def preorder(self, node):
    """
    Travessia em pré-ordem.

    Esta função realiza uma travessia em pré-ordem na árvore binária. A
    travessia em pré-ordem visita o nó atual, em seguida, recursivamente
    visita a subárvore esquerda e, por fim, a subárvore direita.

    Argumentos:
        node: O nó atual a ser visitado na travessia.

    Retorno:
        Nenhum. (A função imprime os valores dos nós na tela)
    """
    if node is not None:
      print(node.value)
      self.preorder(node.left)
      self.preorder(node.right)

  def inorder(self, node):
    """
    Travessia em ordem.

    Esta função realiza uma travessia em ordem na árvore binária. A
    travessia em ordem visita recursivamente a subárvore esquerda, em seguida,
    visita o nó atual e, por fim, a subárvore direita.

    Argumentos:
        node: O nó atual a ser visitado na travessia.

    Retorno:
        Nenhum. (A função imprime os valores dos nós na tela)
    """
    if node is not None:
      self.inorder(node.left)
      print(node.value)
      self.inorder(node.right)

  def postorder(self, node):
    """
    Travessia em pós-ordem.

    Esta função realiza uma travessia em pós-ordem na árvore binária. A
    travessia em pós-ordem visita recursivamente a subárvore esquerda, em
    seguida a subárvore direita e, por fim, o nó atual.

    Argumentos:
        node: O nó atual a ser visitado na travessia.

    Retorno:
        Nenhum. (A função imprime os valores dos nós na tela)
    """
    if node is not None:
      self.postorder(node.left)
      self.postorder(node.right)
      print(node.value)


# Exemplo de uso
tree = Tree()

# Inserir alguns valores
tree.insert(10)
tree.insert(5)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(60)
# Buscar um valor
value = 15
if tree.search(value):
  print(f"O valor {value} foi encontrado na árvore.")
else:
  print(f"O valor {value} não foi encontrado na árvore.")

# Remover um valor
value = 50
tree.remove(value)
print(f"Após remover o valor {value}:")
tree.preorder(tree.root)

# Travessias
print("\nTravessia em pré-ordem:")
tree.preorder(tree.root)
print("\nTravessia em ordem:")
tree.inorder(tree.root)
print("\nTravessia em pós-ordem:")
tree.postorder(tree.root)