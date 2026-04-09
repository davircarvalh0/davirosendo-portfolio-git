# Registro de Resolução de Conflito

**1. O que causou o conflito?**
O conflito ocorreu no arquivo `relatorio.txt`. Ele foi gerado porque duas branches diferentes (`fix/realidade-a` e `fix/realidade-b`) alteraram exatamente a mesma linha de texto nesse arquivo simultaneamente, partindo de um mesmo commit original na branch `main`. Ao fazer o primeiro merge, a alteração da branch A foi aceita. Porém, ao tentar fazer o merge da branch B logo em seguida, o Git encontrou uma colisão de informações na mesma linha e pausou o processo, pois não soube qual versão priorizar.

**2. Como a decisão foi tomada?**
Abri o arquivo no editor de código (VS Code) e analisei as duas opções separadas pelos marcadores automáticos do Git (`<<<<<<< HEAD`, `=======` e `>>>>>>> fix/realidade-b`). Para resolver, apaguei as marcações geradas pelo Git e decidi criar uma versão unificada que fizesse sentido para ambas as realidades. O texto escolhido para permanecer no arquivo final foi: "Status: Finalizado por ambas as branches".

**3. Como o conflito foi marcado como resolvido?**
Após salvar o arquivo com a versão final corrigida, retornei ao terminal e utilizei o comando `git add .` para informar ao Git que o conflito foi tratado. Em seguida, concluí o processo com o comando `git commit -m "fix(ex03): resolve conflito entre as branches A e B e adiciona registro"`, o que concretizou o merge conflitante e limpou o estado do repositório.