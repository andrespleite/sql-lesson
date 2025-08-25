import sqlite3
import pandas as pd

def test_select_scu_clientes(conn, query):
    """Testa a query SELECT - setor, cidade e uf dos clientes"""
    expected_data = {
        'setor': ['Tecnologia', 'Agronegócio', 'Metalurgia', 'Educação', 'Logística'],
        'cidade': ['São Paulo', 'Campinas', 'Santos', 'Ribeirão Preto', 'São José dos Campos'],
        'uf': ['SP', 'SP', 'SP', 'SP', 'SP']
    }
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False

def test_select_2_clientes(conn, query):
    """Testa a query SELECT"""
    expected_data = {
    'id': [1, 9, 10],
    'nome': ['TechCorp Solutions', 'BeachTech Inovação', 'TurisRio Hospedagem'],
    'setor': ['Tecnologia', 'Tecnologia', 'Turismo'],
    'cidade': ['São Paulo', 'Niterói', 'Cabo Frio'],
    'uf': ['SP', 'RJ', 'RJ']
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False
    
def test_select_3(conn, query):
    """Testa a query SELECT """
    expected_data = {
    'id': [1, 4, 5, 7],
    'projeto_id': [1, 2, 3, 4],
    'consultor_id': [1, 5, 1, 5],
    'horas_trabalhadas': [120.5, 110.0, 150.0, 200.0]
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False

def test_select_4(conn, query):
    """Testa a query SELECT """
    expected_data = {
   'id': [7, 5, 1, 4],
   'projeto_id': [4, 3, 1, 2],
   'consultor_id': [5, 1, 1, 5],
   'horas_trabalhadas': [200.0, 150.0, 120.5, 110.0]
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False
    

def test_select_5(conn, query):
    """Testa a query SELECT """
    expected_data = {
   'id': [7],
   'projeto_id': [4],
   'consultor_id': [5],
   'horas_trabalhadas': [200.0]
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False
    

def test_ex1(conn, query):
    """Testa a query SELECT """
    expected_data = {
    'pior_projeto': [5]
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False
    
def test_ex2(conn, query):
    """Testa a query SELECT """
    expected_data = {
    'nao_acabou': ['LOGISTICA III', 'VENDAS V', 'FINANCEIRO VI']
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False
    
def test_ex3(conn, query):
    """Testa a query SELECT """
    expected_data = {
    'finalizados': ['ERP I', 'MARKETING II']
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False
    
def test_ex4(conn, query):
    """Testa a query SELECT """
    expected_data = {
    'horas_trabalhadas': [80.0, 95.5, 85.5, 90.0]
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False
    
def test_ex5(conn, query):
    """Testa a query SELECT """
    expected_data = {
    'nome': ['TechCorp Solutions','Verde Agro Ltda','MetalMax Indústrias','EduCare Ensino','FastLogistic S.A.','Café Premium Montanhas']
}
    expected_df = pd.DataFrame(expected_data)
    
    try:
        # Usar a query do usuário se fornecida, caso contrário usar a query do gabarito
        query_to_test = query if query else """
            SELECT setor, cidade uf 
            FROM clientes
        """
        resultado = pd.read_sql_query(query_to_test, conn)
        
        # Sempre mostrar os dois DataFrames para comparação
        print("\nRESULTADO ESPERADO:")
        print("=" * 50)
        print(expected_df.to_string(index=False))
        print("\n📊 SEU RESULTADO:")
        print("=" * 50)
        print(resultado.to_string(index=False))
        print("\n")
        
        # Agora fazer a validação
        try:
            pd.testing.assert_frame_equal(
                expected_df.sort_index(axis=1).reset_index(drop=True),
                resultado.sort_index(axis=1).reset_index(drop=True),
                check_dtype=False
            )
            print("✅ PASSOU: SELECT - setor, cidade e uf dos clientes")
            return True
        except AssertionError:
            print("❌ FALHOU: Os resultados não são iguais")
            print("💡 Dica: Verifique se você selecionou apenas as colunas pedidas na ordem correta")
            return False
            
    except Exception as e:
        print(f"❌ FALHOU: Erro ao executar query - {str(e)}")
        return False