#include <iostream>

#include <string> // 	std::string nome2  = "Augusto"; Dessa forma eu consigo alterar a info do array


// <tipo de retorno> <nome> (<argumentos...>) { <escopo>}


void PrintTest(int x){ // Se adicionar o & a var�avel � alterada dentro do main, caso n�o continua a mesma coisa.
	std::cout << x << " Teste!\n";
}


int MySum(int x,int y){
	return x + y;
}

struct Humano {
public:
	Humano(){
		name = "Humano";
		age = 0;
		height = 0.f;
		weight = 0.f;
	}
	Humano(std::string n, int age = 0){
		this->name = n;
		this->age = age;
		this->height = 0.f;
		this->weight = 0.f;
	}
	void ShowID(){
		std::cout << "Name : " << name << "\n";
		std::cout << "Age : " << age << "\n";
		std::cout << "Height : " << height << "\n";
		std::cout << "Weight: " << weight << "\n";
	}
	
	void Birthday() {
		age++;
		std::cout << name << " now is " << age << " years old!\n";
	}
private:
	std::string name;
	
	int age;
	float height;
	float weight;
};
int main() { 
	
	// print usando C++, cout - abrevia��o de console output
	// std::cout << "Hellow World!\n";]
	int myArray[10];
	int x = 10;
	int y = 5;
	int z; 
	z = MySum(x, y);
	std::cout << z << "\n";
	for (int i = 0; i < 10; i ++){
		PrintTest(i);
		myArray[i] = i + i;
	}

	
	Humano saboia("Saboia", 20);
	for (int x = 0; x < 10; x++){
	saboia.Birthday();
}
	saboia.ShowID();
	
	return 0;
}
