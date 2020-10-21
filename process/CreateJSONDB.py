import pandas as pd
import json
import random
import math

from log.Log import Log
from log.PreProcess import PreProcess
from process.MacroSteps import MacroSteps


# link 'grupos' and 'varas'


path_clusters = '/home/vercosa/Insync/doutorado/hackaton_cnj/'+\
              'projeto_git/desafio_cnj/data/interim/'+\
              'clusterizacao_varas.csv'

file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'versao5/version_5.csv'

# file_dados_basicos = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
#                      'dados_basicos_estadual/df_dadosbasicos_justica_estadual.csv'

movement_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
                'projeto_git/desafio_cnj/data/interim/df_movimentos.csv'

lat_long_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
                'projeto_git/desafio_cnj/data/interim/' + \
                'municipios_lat_long.csv'

comments_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
                'projeto_git/desafio_cnj/data/interim/praticas.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}


df_log = pd.read_csv(file_path,
                     dtype=datatypes,
                     sep=';', 
                     engine='python')



df_proc = df_log[['case: orgao_mun', 'case:concept:name']].drop_duplicates()
df_proc = df_proc.groupby('case: orgao_mun').count().\
    sort_values(by='case:concept:name')
df_proc = df_proc.rename(columns={'case:concept:name':'process_count'})
df_proc.reset_index(level=0, inplace=True)
df_proc['case: orgao_mun'] = df_proc['case: orgao_mun'].str.upper()
df_proc['case: orgao_mun'] = df_proc['case: orgao_mun'].str.replace('"','')
df_proc['case: orgao_mun'] = df_proc['case: orgao_mun'].\
    str.replace(' - ','-')
df_proc['case: orgao_mun'] = df_proc['case: orgao_mun'].\
    str.replace('-',' - ')
df_proc = df_proc[df_proc['process_count'] >= 50]






# check how many encoding errors
l1 = [x for x in df_proc['case: orgao_mun'].unique().tolist()] 
l2 = [x for x in df_proc['case: orgao_mun'].unique().tolist()] 
l2 = [x.encode('latin-1', errors='ignore').decode('latin-1') for x in l2]

count = 0 

for i in range(len(l1)): 
    if l1[i] == l2[i]: 
        count += 1 

count


df_clusters = pd.read_csv(path_clusters,
                        sep=';',
                        engine='python')

df_clusters['Orgao Julgador'] = df_clusters['Orgao Julgador'].str.upper()
df_clusters = df_clusters.rename(columns={'Orgao Julgador':'case: orgao_mun'})
df_clusters['case: orgao_mun'] = df_clusters['case: orgao_mun'].\
    str.replace(' - ','-')
df_clusters['case: orgao_mun'] = df_clusters['case: orgao_mun'].\
    str.replace('-',' - ')

alg = 'TSNE'

df_clusters_alg = df_clusters[['case: orgao_mun', alg]]

df_proc = df_proc.merge(df_clusters_alg, on='case: orgao_mun', how='left')

df_temp = df_proc.groupby(alg).count().sort_values(by='case: orgao_mun')

df_temp

df_temp.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                           '/versao5/grupos_cluster.csv', sep=';')


# create 'grupos' json
    # group_id: <cluster_id>
    # justice: 'states'
    # grade: 'G1'
    # competences: 1116
    # subject: 'Execução Fiscal'
    # method: 'TSNE + DBSCAN'
    # amount_of_varas: <#cluster_members>

# selected groups
    # id: 111, varas: 57
    # id: 98, varas: 17
    # id: 256, varas: 16

json_group = []

group1 = {
    'pk':111,
    'model':'performance.Group',
    'fields':{
        'group_id': 111,
        'justice': 'states',
        'grade': 'G1',
        'competences': 1116,
        'subject': 'Execução Fiscal',
        'method': 'TSNE + DBSCAN',
        'amount_of_varas': 51
    }
}

group2 = {
    'pk':98,
    'model':'performance.Group',
    'fields':{
        'group_id': 98,
        'justice': 'states',
        'grade': 'G1',
        'competences': 1116,
        'subject': 'Execução Fiscal',
        'method': 'TSNE + DBSCAN',
        'amount_of_varas': 12
    }
}

group3 = {
    'pk':256,
    'model':'performance.Group',
    'fields':{
        'group_id': 256,
        'justice': 'states',
        'grade': 'G1',
        'competences': 1116,
        'subject': 'Execução Fiscal',
        'method': 'TSNE + DBSCAN',
        'amount_of_varas': 14
    }
}

json_group.append(group1)
json_group.append(group2)
json_group.append(group3)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_groups.json', 'w') as f:
          json.dump(json_group, f)



# create cadastro_etapas objects
    # step_id
    # origin
    # destination

macrosteps = [
              
              'Distribuição', 
              'Conclusão',
              'Despacho',
              'Decisão',
              'Julgamento',
              'Trânsito em julgado', 
              'Baixa/Arquivamento',  
             ]

json_step_config = []
json_step_config_map = {}

step_config_id = 20

for m in macrosteps:
    for m2 in macrosteps:
        json_aux = {'model':'performance.StepConfiguration'}
        json_aux['pk'] = step_config_id
        json_aux['fields'] = {}
        json_aux['fields']['step_id'] = step_config_id
        json_aux['fields']['origin'] = m
        json_aux['fields']['destination'] = m2
        json_step_config.append(json_aux)

        json_step_config_map[m + ' -> ' + m2] = step_config_id

        step_config_id += 1


# create comments


df_comments = pd.read_csv(comments_path,
                          sep=',', 
                          engine='python')

comments_list = df_comments['Pratica'].tolist()
len_comments = len(comments_list)
json_comments = []
count_comments = 20

for c in comments_list:
    json_comments_aux = {"model": "performance.Comments",
                         "pk": str(count_comments)}
    json_comments_aux["fields"] = {"comment_id": count_comments,
                                   "comment": c}
    json_comments.append(json_comments_aux)
    count_comments += 1

# create vara objects
    # vara_id
    # nome
    # processos_julgados
    # movimentacoes
    # identificador_grupo
    # dias_baixa_processo
    
    # tempo_macroetapa1 (Distribuição)
    # tempo_macroetapa2 (Conclusão)
    # tempo_macroetapa3 (Despacho) 
    # tempo_macroetapa4 (Decisão)
    # tempo_macroetapa5 (Julgamento)
    # tempo_macroetapa6 (Trânsito em julgado)
    # tempo_macroetapa7 (Baixa/Arquivamento)


# selected groups
    # 256
    # 98
    # 111


varas_dict = {}

varas_dict[256] = df_proc[(df_proc['TSNE'] == 256)]\
                    ['case: orgao_mun'].tolist()

varas_dict[111] = df_proc[(df_proc['TSNE'] == 111)]\
                    ['case: orgao_mun'].tolist()

varas_dict[98] = df_proc[(df_proc['TSNE'] == 98)]\
                    ['case: orgao_mun'].tolist()


pp = PreProcess(file_location=file_path)
pp.select_desired_columns()
pp.filter_outlier_timestamp()
pp.map_movements(movement_path)

df_log = pp.df_log
df_log['case: orgao_mun'] = df_log['case: orgao_mun'].str.upper()
df_log['case: orgao_mun'] = df_log['case: orgao_mun'].str.replace('"','')
df_log['case: orgao_mun'] = df_log['case: orgao_mun'].\
    str.replace(' - ','-')
df_log['case: orgao_mun'] = df_log['case: orgao_mun'].\
    str.replace('-',' - ')

# get latitude and longitude

df_lat_long = pd.read_csv(lat_long_path)
df_lat_long = df_lat_long[['codigo_ibge', 'latitude', 'longitude']]

df_aux = df_log[['case: orgao_mun', 'case: municipio']].\
            drop_duplicates(subset=['case: orgao_mun'])
df_aux = df_aux.rename(columns={'case: municipio': 'codigo_ibge'})
df_aux = df_aux.merge(df_lat_long, on='codigo_ibge', how='left')
map_lat_long = df_aux.set_index('case: orgao_mun').to_dict()

json_vara = []
json_steps = []
vara_id_count = 20
step_id_count = 20
number_of_skips = {}
ranking_varas = {}

for group in varas_dict:

    number_of_skips[group] = 0
    ranking_varas[group] = {}

    for vara in varas_dict[group]:

        json_vara_aux = {'model':'performance.Vara',
                        'pk':vara_id_count,
                        'fields':{}
                        }

        vara_id = vara_id_count
        name = vara
        latitude = map_lat_long['latitude'][name]
        longitude = map_lat_long['longitude'][name]

        if math.isnan(latitude):
            latitude = None
        
        if math.isnan(longitude):
            longitude = None

        json_vara_aux['fields']['vara_id'] = vara_id
        json_vara_aux['fields']['name'] = name
        json_vara_aux['fields']['latitude'] = latitude
        json_vara_aux['fields']['longitude'] = longitude

        df_vara = df_log[df_log['case: orgao_mun'] == vara]
        pp_vara = PreProcess(df=df_vara)
        pp_vara.filter_outlier_movements(lower=0.05, upper=0.95)
        pp_vara.filter_outlier_trace_time(lower=0.05, upper=0.95)
        df_vara = pp_vara.df_log

        log = Log(df_log=pp_vara.df_log.sort_values('time:timestamp'))

        finished_processes = int(df_vara['case:concept:name'].\
            drop_duplicates().count())
        print('finished_processes: ', str(finished_processes))
        json_vara_aux['fields']['finished_processes'] = finished_processes

        total_movements = int(df_vara['case:concept:name'].count())

        movements = \
            int(total_movements / finished_processes)
        print('movements: ', str(movements))
        json_vara_aux['fields']['movements'] = movements

        group_id = group
        days_finish_process = int(log.median_time() / (24*60*60))
        print('days_finish_process: ', str(days_finish_process))
        json_vara_aux['fields']['group_id'] = group_id
        json_vara_aux['fields']['days_finish_process'] = days_finish_process
        ranking_varas[group][vara_id] = days_finish_process

        if movements > 5 and days_finish_process > 0:

            ms = MacroSteps(log.log, macrosteps)
            macrosteps_result = ms.calc_macrosteps()
            # print('')
            # print('macrosteps: ', str(macrosteps_result))
            # print('')

            # rescale macrosteps
            # total = sum(macrosteps_result.values())

            # for m in macrosteps_result:
            #     macrosteps_result[m] = int((macrosteps_result[m] / total)\
            #         * days_finish_process)

            # print('macrosteps: ', str(macrosteps_result))

            for m in macrosteps_result:
                if m == 'Distribuição':
                    json_vara_aux['fields']['time_distribuicao'] = \
                        int(macrosteps_result[m])

                if m == 'Conclusão':
                    json_vara_aux['fields']['time_conclusao'] = \
                        int(macrosteps_result[m])

                if m == 'Despacho':
                    json_vara_aux['fields']['time_despacho'] = \
                        int(macrosteps_result[m])

                if m == 'Decisão':
                    json_vara_aux['fields']['time_decisao'] = \
                        int(macrosteps_result[m])

                if m == 'Julgamento':
                    json_vara_aux['fields']['time_julgamento'] = \
                        int(macrosteps_result[m])

                if m == 'Trânsito':
                    json_vara_aux['fields']['time_transito_em_julgado'] = \
                        int(macrosteps_result[m])

                if m == 'Baixa':
                    json_vara_aux['fields']['time_baixa_ou_arquivamento'] = \
                        int(macrosteps_result[m])
        
            json_vara.append(json_vara_aux)

            # create json Steps

            macro_trace_freq = ms.get_macro_trace(freq=True)
            macro_trace_time = ms.get_macro_trace(freq=False)

            # rescale macrosteps
            total = sum(macro_trace_time.values())

            # for m in macrosteps_result:
            #     macrosteps_result[m] = int((macrosteps_result[m] / total)\
            #         * days_finish_process)

            # print('')
            # print('macro_trace_freq: ', str(macro_trace_freq))
            # print('macro_trace_time: ', str(macro_trace_time))
            # print('')


            for m in macro_trace_freq:
                if macro_trace_time[m] > 0:
                    json_steps_aux = {'model':'performance.Steps',
                                'pk':step_id_count,
                                'fields':{}
                                }
                    json_steps_aux['fields']['step_id'] = \
                        json_step_config_map[m]
                    json_steps_aux['fields']['vara_id'] = \
                        vara_id_count
                
                    json_steps_aux['fields']['frequency'] = \
                        macro_trace_freq[m]
                    json_steps_aux['fields']['med_time'] = \
                        macro_trace_time[m]
                    json_steps_aux['fields']['comment_id'] = \
                        20 + int(random.random()*len_comments)

                    json_steps.append(json_steps_aux)
                    
                    step_id_count += 1


            # print('current json_steps:')
            # print(json_steps)

            vara_id_count += 1 
        else:
            number_of_skips[group] += 1


# add ranking

for group in ranking_varas:
    ranking_varas[group] = \
        {k: v for k, v in sorted(ranking_varas[group].items(), 
                                 key=lambda item: item[1])}

print('ranking_varas: ', str(ranking_varas))

for vara in json_vara:
    vara['fields']['ranking'] = \
        list(ranking_varas[vara['fields']['group_id']]).\
            index(vara['pk']) + 1



with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_varas.json', 'w') as f:
          json.dump(json_vara, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_steps.json', 'w') as f:
          json.dump(json_steps, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_steps.json', 'w') as f:
          json.dump(json_steps, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_steps_config.json', 'w') as f:
          json.dump(json_step_config, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_comments.json', 'w') as f:
          json.dump(json_comments, f)
          