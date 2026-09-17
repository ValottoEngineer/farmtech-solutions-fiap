# FarmTech Solutions - Estatisticas basicas (R)
# Le os dados exportados pelo app Python (dados_talhoes.csv) e calcula
# media e desvio padrao das principais medidas, geral e por cultura.

arquivo_csv <- "dados_talhoes.csv"

if (!file.exists(arquivo_csv)) {
  stop(paste0(
    "Arquivo '", arquivo_csv, "' nao encontrado.\n",
    "Rode antes o farm-tech_app.py e cadastre ao menos um talhao ",
    "(ele exporta o CSV automaticamente), ou rode este script na pasta do projeto."
  ))
}

dados <- read.csv(arquivo_csv, stringsAsFactors = FALSE, fileEncoding = "UTF-8")

cat("=============================================\n")
cat("  FarmTech Solutions - Estatisticas (R)\n")
cat("=============================================\n\n")

if (nrow(dados) == 0) {
  cat("Nenhum talhao cadastrado ainda em", arquivo_csv, "\n")
  quit(status = 0)
}

cat("Total de talhoes cadastrados:", nrow(dados), "\n\n")

colunas_numericas <- c(
  "largura_m", "comprimento_m", "area_m2",
  "num_ruas", "taxa_ml_por_metro", "volume_litros"
)

calcular_desvio <- function(valores) {
  if (length(valores) > 1) sd(valores) else NA
}

cat("--- Estatisticas gerais (todas as culturas) ---\n")
for (coluna in colunas_numericas) {
  media <- mean(dados[[coluna]])
  desvio <- calcular_desvio(dados[[coluna]])
  texto_desvio <- if (is.na(desvio)) "N/A" else sprintf("%.2f", desvio)
  cat(sprintf("%-18s media = %12.2f | desvio padrao = %s\n", coluna, media, texto_desvio))
}

cat("\n--- Estatisticas por cultura ---\n")
culturas <- unique(dados$cultura)
for (cultura_atual in culturas) {
  subset_dados <- dados[dados$cultura == cultura_atual, ]
  cat(sprintf("\nCultura: %s (n = %d)\n", cultura_atual, nrow(subset_dados)))
  for (coluna in colunas_numericas) {
    media <- mean(subset_dados[[coluna]])
    desvio <- calcular_desvio(subset_dados[[coluna]])
    texto_desvio <- if (is.na(desvio)) "N/A (n=1)" else sprintf("%.2f", desvio)
    cat(sprintf("  %-16s media = %12.2f | desvio padrao = %s\n", coluna, media, texto_desvio))
  }
}
