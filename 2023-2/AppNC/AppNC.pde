PImage fundoMenu;  // Imagem de fundo do menu
PImage fundoMapa;  // Imagem de fundo do mapa
PImage botaoIniciar;  // Botão "Iniciar"
PImage botaoSair;  // Botão "Sair"
PImage iconeFase1;  // Ícone da Fase 1
PImage iconeFase2;  // Ícone da Fase 2
PImage iconeFase3;  // Ícone da Fase 3
PImage fundoFase1; // Imagem de fundo da Fase 1
PImage sequen0; // Sequência de cores
PImage escolh1; // Escolha 1
PImage escolh2; // Escolha 2
PImage escolh3; // Escolha 3
PImage escolh4; // Escolha 4
PImage telaVitoria; // Imagem de tela de vitória
PImage telaDerrota; // Imagem de tela de derrota
PImage escolhaCorreta1;
PImage escolhaCorreta2;
PImage escolhaCorreta3;
PImage escolhaCorreta4;

// Imagens da Fase 2
PImage fundoFase2; // Imagem de fundo da Fase 2
PImage numero1;  // Imagem do número 1
PImage numero2;  // Imagem do número 2
PImage numero3;  // Imagem do número 3
PImage numero4;  // Imagem do número 4
PImage condicao1;  // Imagem da condição 1
PImage condicao2;  // Imagem da condição 2
PImage barraCalculos;  // Imagem da barra de cálculos

// Imagens da Fase 3
PImage fundoFase3; // Imagem de fundo da Fase 3
PImage sequenciaCores; // Imagem da sequência de cores
PImage selecaoCor1; // Imagem da seleção de cor 1
PImage selecaoCor2; // Imagem da seleção de cor 2
PImage selecaoCor3; // Imagem da seleção de cor 3
PImage selecaoCor4; // Imagem da seleção de cor 4
PImage repeticao1; // Primeira imagem de repetição
PImage repeticao2; // Segunda imagem de repetição
PImage repeticao3; // Terceira imagem de repetição
PImage repeticao4; // Quarta imagem de repetição

boolean inMenu = true;
boolean inMapa = false;
boolean inFase1 = false;
boolean inFase2 = false;
boolean inFase3 = false;
boolean vitoria = false;
boolean derrota = false;

int fase1Order = 0; // Variável para rastrear a ordem das escolhas
int vitoriaTimer = 0; // Temporizador para a tela de vitória
int derrotaTimer = 0; // Temporizador para a tela de derrota

void setup() {
  size(1080, 540);
  background(255);

  // Carregando as imagens (substitua os nomes dos arquivos pelas imagens corretas)
  fundoMenu = loadImage("fundoMenu.png");
  fundoMapa = loadImage("fundoMapa.png");
  botaoIniciar = loadImage("botaoIniciar.png");
  botaoSair = loadImage("botaoSair.png");
  iconeFase1 = loadImage("iconeFase1.png");
  iconeFase2 = loadImage("iconeFase2.png");
  iconeFase3 = loadImage("iconeFase3.png");
  fundoFase1 = loadImage("fundoFase1.png");
  sequen0 = loadImage("sequen0.png");
  escolh1 = loadImage("escolh1.png");
  escolh2 = loadImage("escolh2.png");
  escolh3 = loadImage("escolh3.png");
  escolh4 = loadImage("escolh4.png");
  telaVitoria = loadImage("telaVitoria.png");
  telaDerrota = loadImage("telaDerrota.png");
  escolhaCorreta1 = loadImage("escolhaCorreta1.png");
  escolhaCorreta2 = loadImage("escolhaCorreta2.png");
  escolhaCorreta3 = loadImage("escolhaCorreta3.png");
  escolhaCorreta4 = loadImage("escolhaCorreta4.png");

  // Carregando as imagens da Fase 2
  fundoFase2 = loadImage("fundoFase2.png");
  numero1 = loadImage("numero1.png");
  numero2 = loadImage("numero2.png");
  numero3 = loadImage("numero3.png");
  numero4 = loadImage("numero4.png");
  condicao1 = loadImage("condicao1.png");
  condicao2 = loadImage("condicao2.png");
  barraCalculos = loadImage("barraCalculos.png");

  // Carregando as imagens da Fase 3
  fundoFase3 = loadImage("fundoFase3.png");
  sequenciaCores = loadImage("sequenciaCores.png");
  selecaoCor1 = loadImage("selecaoCor1.png");
  selecaoCor2 = loadImage("selecaoCor2.png");
  selecaoCor3 = loadImage("selecaoCor3.png");
  selecaoCor4 = loadImage("selecaoCor4.png");
  repeticao1 = loadImage("repeticao1.png");
  repeticao2 = loadImage("repeticao2.png");
  repeticao3 = loadImage("repeticao3.png");
  repeticao4 = loadImage("repeticao4.png");
}

void draw() {
  background(255);  // Limpa a tela

  if (inMenu) {
    // Exibe o fundo do menu
    image(fundoMenu, 0, 0);

    // Botão "Iniciar"
    image(botaoIniciar, 0, 0, 1080, 540);
    if (isImageClicked(botaoIniciar) && mousePressed) {
      inMenu = false;
      inMapa = true;
      vitoria = false;
      derrota = false;
    }

    // Botão "Sair"
    image(botaoSair, 0, 0, 1080, 540);
    if (isImageClicked(botaoSair) && mousePressed) {
      exit();  // Fecha o aplicativo
    }
  } else if (inMapa) {
    // Exibe o fundo do mapa
    image(fundoMapa, 0, 0);

    // Botões de acesso às fases
    image(iconeFase1, 0, 0, 1080, 540);
    if (isImageClicked(iconeFase1) && mousePressed) {
      inMapa = false;
      inFase1 = true;
      vitoria = false;
      derrota = false;
      fase1Order = 0; // Reinicializa a ordem da fase 1
    }

    image(iconeFase2, 0, 0, 1080, 540);
    if (isImageClicked(iconeFase2) && mousePressed) {
      inMapa = false;
      inFase2 = true;
      vitoria = false;
      derrota = false;
    }

    image(iconeFase3, 0, 0, 1080, 540);
    if (isImageClicked(iconeFase3) && mousePressed) {
      inMapa = false;
      inFase3 = true;
      vitoria = false;
      derrota = false;
    }
  } else if (inFase1) {
    // Exibe o fundo da Fase 1
    image(fundoFase1, 0, 0);
    
    if (fase1Order == 0) {
      // Exibe a sequência de cores
      image(sequen0, 0, 0, 1080, 540);
      if (millis() > 5000) {
        fase1Order++;
      }
    } else if (fase1Order == 1) {
      // Exibe a escolha 1
      image(escolh1, 0, 0, 1080, 540);
      if (isImageClicked(escolh1) && mousePressed) {
        fase1Order++;
        image(escolhaCorreta1, 0, 0, 1080, 540);
      }
    } else if (fase1Order == 2) {
      // Exibe a escolha 4
      image(escolh4, 0, 0, 1080, 540);
      if (isImageClicked(escolh4) && mousePressed) {
        fase1Order++;
        image(escolhaCorreta2, 0, 0, 1080, 540);
      }
    } else if (fase1Order == 3) {
      // Exibe a escolha 2
      image(escolh2, 0, 0, 1080, 540);
      if (isImageClicked(escolh2) && mousePressed) {
        fase1Order++;
        image(escolhaCorreta3, 0, 0, 1080, 540);
      }
    } else if (fase1Order == 4) {
      // Exibe a escolha 3
      image(escolh3, 0, 0, 1080, 540);
      if (isImageClicked(escolh3) && mousePressed) {
        fase1Order++;
        image(escolhaCorreta4, 0, 0, 1080, 540);
      }
      if (isImageClicked(escolh1) && isImageClicked(escolh4) && isImageClicked(escolh2) && isImageClicked(escolh3)) {
        vitoria = true;
      } else {
        derrota = true;
      }
    }
  } else if (inFase2) {
    // Exibe o fundo da Fase 2
    image(fundoFase2, 0, 0);
    
    // Exibe as imagens da Fase 2
    image(numero1, 0, 0, 1080, 540);
    image(numero2, 0, 0, 1080, 540);
    image(numero3, 0, 0, 1080, 540);
    image(numero4, 0, 0, 1080, 540);
    image(condicao1, 0, 0, 1080, 540);
    image(condicao2, 0, 0, 1080, 540);
    image(barraCalculos, 0, 0, 1080, 540);
  } else if (inFase3) {
    // Exibe o fundo da Fase 3
    image(fundoFase3, 0, 0);
    
    // Exibe as imagens da Fase 3
    image(sequenciaCores, 0, 0, 1080, 540);
    image(selecaoCor1, 0, 0, 1080, 540);
    image(selecaoCor2, 0, 0, 1080, 540);
    image(selecaoCor3, 0, 0, 1080, 540);
    image(selecaoCor4, 0, 0, 1080, 540);
    image(repeticao1, 0, 0, 1080, 540);
    image(repeticao2, 0, 0, 1080, 540);
    image(repeticao3, 0, 0, 1080, 540);
    image(repeticao4, 0, 0, 1080, 540);

   
  } else if (vitoria) {
    // ...
  } else if (derrota) {
    // ...
  }
}


boolean isImageClicked(PImage img) {
  int x = mouseX;
  int y = mouseY;
  if (x >= 0 && x < img.width && y >= 0 && y < img.height) {
    color c = img.get(x, y);
    return alpha(c) > 0; 
  }
  return false;
}
