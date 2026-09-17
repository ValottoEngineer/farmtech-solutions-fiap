# FarmTech Solutions - Clima (R + API meteorologica publica, sem chave)
# Usa a API gratuita Open-Meteo (geocodificacao + previsao atual) para
# mostrar as condicoes climaticas da lavoura em texto simples no terminal.

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Pacote 'jsonlite' nao encontrado. Instale com: install.packages(\"jsonlite\")")
}

library(jsonlite)

cat("=============================================\n")
cat("  FarmTech Solutions - Clima (R + API publica)\n")
cat("=============================================\n\n")

cat("Digite a cidade da lavoura (ex: Franca, SP) [Enter = Franca]: ")
cidade <- trimws(readLines("stdin", n = 1))
if (length(cidade) == 0 || cidade == "") {
  cidade <- "Franca"
}

geocode_url <- paste0(
  "https://geocoding-api.open-meteo.com/v1/search?name=",
  URLencode(cidade), "&count=1&language=pt&format=json"
)

geo <- fromJSON(geocode_url)

if (is.null(geo$results)) {
  stop(paste("Nao foi possivel encontrar a cidade:", cidade))
}

local_encontrado <- geo$results[1, ]
lat <- local_encontrado$latitude
lon <- local_encontrado$longitude
nome_local <- local_encontrado$name
uf <- if ("admin1" %in% names(local_encontrado)) local_encontrado$admin1 else ""

forecast_url <- paste0(
  "https://api.open-meteo.com/v1/forecast?latitude=", lat,
  "&longitude=", lon,
  "&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,weather_code",
  "&timezone=auto"
)

previsao <- fromJSON(forecast_url)
atual <- previsao$current

descrever_tempo <- function(codigo) {
  descricoes <- c(
    "0" = "Ceu limpo", "1" = "Predominantemente limpo", "2" = "Parcialmente nublado",
    "3" = "Nublado", "45" = "Neblina", "48" = "Neblina com geada",
    "51" = "Garoa fraca", "53" = "Garoa moderada", "55" = "Garoa forte",
    "61" = "Chuva fraca", "63" = "Chuva moderada", "65" = "Chuva forte",
    "71" = "Neve fraca", "80" = "Pancadas de chuva fracas", "81" = "Pancadas de chuva moderadas",
    "82" = "Pancadas de chuva fortes", "95" = "Tempestade"
  )
  chave <- as.character(codigo)
  if (chave %in% names(descricoes)) descricoes[[chave]] else "Condicao desconhecida"
}

cat("\nLocal:", nome_local, uf, "\n")
cat(sprintf("Coordenadas: %.4f, %.4f\n", lat, lon))
cat("--------------------------------------------\n")
cat("Temperatura atual:", atual$temperature_2m, "C\n")
cat("Umidade relativa: ", atual$relative_humidity_2m, "%\n")
cat("Precipitacao:     ", atual$precipitation, "mm\n")
cat("Vento:             ", atual$wind_speed_10m, "km/h\n")
cat("Condicao:          ", descrever_tempo(atual$weather_code), "\n")
cat("--------------------------------------------\n")

chuva_codigos <- c(51, 53, 55, 61, 63, 65, 80, 81, 82, 95)
if (atual$precipitation > 0 || atual$weather_code %in% chuva_codigos) {
  cat("\nRecomendacao: condicoes de chuva - evite pulverizacao de insumos agora.\n")
} else if (atual$wind_speed_10m > 15) {
  cat("\nRecomendacao: vento acima de 15 km/h - risco de deriva na pulverizacao.\n")
} else {
  cat("\nRecomendacao: condicoes favoraveis para pulverizacao e manejo de insumos.\n")
}
