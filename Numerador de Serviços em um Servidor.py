#Código feito pelo Engineer-Lucca <-|->
#O código detalhado está logo abaixo , aproveitem, qualquer dúvida só me chamar via chat  : 

# Dicionário que mapeia números de portas aos serviços correspondentes
port_services = {
    21: "FTP",      # Serviço de transferência de arquivos
    22: "SSH",      # Secure Shell (acesso remoto seguro)
    23: "Telnet",   # Protocolo de acesso remoto inseguro
    25: "SMTP",     # Serviço de envio de emails
    53: "DNS",      # Serviço de tradução de nomes de domínio
    80: "HTTP",     # Protocolo de transferência de hipertexto (web)
    110: "POP3",    # Serviço de recebimento de emails
    143: "IMAP",    # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",   # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",  # Banco de dados MySQL
    3389: "RDP",    # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL", # Banco de dados PostgreSQL
    6379: "Redis"   # Banco de dados Redis
}

# Função que realiza a enumeração de serviços
def enumerate_services(ports):
    # Inicializamos uma lista para armazenar os serviços correspondentes
    services = []
    
    # Itera sobre cada porta fornecida na lista de portas
    for port in ports:
        # Verifica se a porta existe no dicionário de serviços
        if port in port_services:
            # Se existir, adicione o serviço correspondente à lista de serviços
            services.append(port_services[port])
        else:
            # Se a porta não estiver mapeada, adicione "Desconhecido"
            services.append("Desconhecido")
    
    return services

# Função principal que lida com a entrada do usuário e exibe o resultado:
def main():
    ports_input = input()
    
    # Converte a string de entrada para uma lista de inteiros (números de portas)
    # Utiliza a função strip() para remover espaços em branco, e o split() para separar por vírgula
    # A list comprehension [int(p) for p in ...] garante que cada item se torne um número inteiro
    ports_list = [int(p) for p in ports_input.strip().split(',')]
    
    # Chama a função de enumeração para obter la lista de serviços correspondentes:
    services = enumerate_services(ports_list)
    
    print(services)


if __name__ == "__main__":
    main()