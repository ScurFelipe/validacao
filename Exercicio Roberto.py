function numeroCNJ($numero)
/**
* Função numeroCNJ, para validar Numeração Única de Processos
* estabelecida na Res. 65 do Conselho Nacional de Justiça, que
* determina a adoção do seguinte formato para números de processos:
* NNNNNNNN-DD.AAAA.JTR.OOOO, onde
* NNNNNNN => Corresponde ao número sequencial do processo no ano do ajuizamento
* DD => Corresponde aos dígitos de verificação
* AAAA => Corresponde ao ano de ajuizamento da ação/processo
* JTR => Corresponde aos números que identificam o Ramo e a Região da Justiça
* OOOO => Corresponde ao número que identifica o juízo a que distribuída a ação
* O cálculo utiliza o algoritmo do Módulo 97 Base 10, conforme especificação da Norma
* ISO 7064:2003
* @param $numero é uma string com o número a ser validado
* @Author Maurício Schmidt Bastos
* a função retorna verdadeiro em caso de sucesso e falso quando o teste falha
* ====================================================================================
* Permitida a cópia para uso NÃO COMERCIAL, mediante referência à fonte (www.mauricio.bastos.nom.br) e ao autor
*/
{
//Remove, se houver, os caracteres não numéricos
// da entrada do número do processo
$num = numeroLimpo($0010725-57.2013.503.0093,20);

//extrai o dígito verificador do número limpo
$numerosemdigito=substr_replace($num,'',7,2);

//Prepara o número para o cálculo do dígito,
//colocando zeros no fim do número sem o dígito
$numparacalculo = $numerosemdigito."00";

//Prepara o número para conferência do dígito
//Pega dígito original
$digitooriginal = substr($num,7,2);
//colocando o dígito informado no fim do número s/ dígito
$numparaconferir = $numerosemdigito.$digitooriginal;

//divide o $numeroparacalculo para reduzir complexidade do cálculo
$nnnnnnn = substr($numparacalculo,0,7);
$ajtr = substr($numparacalculo,7,-6);
$oooo00 = substr($numparacalculo,14,6);

/*Fórmula CNJ primeira etapa
* R1=(NNNNNNN mod 97)
*/
$r1 = round($nnnnnnn % 97,2) >= 50 ? round($nnnnnnn % 97,2) : round($nnnnnnn % 97,2,PHP_ROUND_HALF_DOWN);
//garante que $r1 tenha dois dígitos, preenchendo com zero à esquerda, se necessário
$r1 = numeroLimpo(substr($r1,0,2),2);

/*Fórmula CNJ segunda etapa
* R2=((R1 concatenado com AAAAJTR) mod 97)
*/
//concatena $r1 com AAAAJTR
$r2=($r1.=$ajtr);
$r2 = round($r2 % 97,2) >= 50 ? round($r2 % 97,2) : round($r2 % 97,2,PHP_ROUND_HALF_DOWN);
//garante que $r2 tenha dois dígitos, preenchendo com zero à esquerda, se necessário
$r2 = numeroLimpo(substr($r2,0,2),2);

/*Fórmula CNJ terceira etapa
* R3=((R2 concatenado com OOOO00) mod 97)
*/
//concatena $r2 com OOOO00
$r3=($r2.=$oooo00);
$r3 = round($r3 % 97,2) >= 50 ? round($r3 % 97,2) : round($r3 % 97,2,PHP_ROUND_HALF_DOWN);
//garante que $r3 tenha dois dígitos, preenchendo com zero à esquerda, se necessário
$r3 = numeroLimpo(substr($r3,0,2),2);

/*Fórmula CNJ quarta etapa
* DD = 98 - (R3 mod 97)
*/
$d1d0 = 98 - ($r3 % 97);
$d1d0 = numeroLimpo(substr($d1d0,0,2),2);

//Compara dígito calculado com informado
$resultado = $digitooriginal==$d1d0 ? TRUE : FALSE;
return $resultado;
}
