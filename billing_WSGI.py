import jinja2
import cgi

def application(environ, start_response):
    # This line tells the template loader where to search for template files
    templateLoader = jinja2.FileSystemLoader( searchpath="./" )

    # This creates your environment and loads a specific template
    env = jinja2.Environment(loader=templateLoader)



    tube_list = []
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        tube_list = post.getlist('tube')

    analyte_list = []
    analyte_set = []

    tube_dict = {
        'B1':['sKappa', 'sLambda', 'CD5', 'CD23', 'CD10', 'CD20', 'CD19', 'CD45'],
        'B2':['FMC7', 'CD103', 'CD38', 'CD21', 'CD34', 'HLA-DR', 'CD19', 'CD45'],
        'T1':['sCD3', 'CD57', 'CD5', 'CD4', 'CD7', 'CD8', 'CD2', 'CD45'],
        'T2':['TCRa/b', 'CD56', 'CD16', 'sCD3', 'CD30', 'CD25', 'TCRg/d', 'CD45'],
        'PL1':['cKappa', 'cLambda', 'CD56', 'CD10', 'CD138', 'CD19', 'CD38', 'CD45'],
        'PL2':['CD14', 'CD33', 'CD56', 'CD117', 'CD138', 'CD28', 'CD38', 'CD45'],
        'MRD':['CD56', 'CD13', 'CD7', 'CD117', 'CD34', 'HLA-DR', 'CD19', 'CD45'],
        'ALL':['sKappa', 'sLambda', 'CD38', 'CD10', 'CD34', 'sCD3', 'CD19', 'CD45'],
        'Cytoplasmics':['cTdT', 'cMPO', 'CD33', 'CD13', 'CD34', 'cCD3', 'CD19', 'CD45'],
        'ALOT':['CD45', 'cCD3', 'CD19', 'CD34', 'cMPO', 'cCD79a', 'CD7', 'CD10'],
        'AML1':['CD45', 'HLA-DR', 'CD117', 'CD34', 'CD16', 'CD13', 'CD11b', 'CD10'],
        'AML2':['CD45', 'HLA-DR', 'CD117', 'CD34', 'CD35', 'CD64', 'CD300e', 'CD14'],
        'AML3':['CD45', 'HLA-DR', 'CD117', 'CD34', 'CD36', 'CD105', 'CD33', 'CD71'],
        'AML4':['CD45', 'HLA-DR', 'CD117', 'CD34', 'cTdT', 'CD56', 'CD7', 'CD19'],
        'AML5':['CD45', 'HLA-DR', 'CD117', 'CD34', 'CD15', 'NG2', 'CD22', 'CD38'],
        'AML6':['CD45', 'HLA-DR', 'CD117', 'CD34', 'CD42a+CD61', 'CD203c', 'CD123', 'CD4'],
        'AML7':['CD45', 'HLA-DR', 'CD117', 'CD34', 'CD41', 'CD25', 'CD42b', 'CD9'],
        'ALL1':['CD45', 'CD19', 'CD34', 'CD20', 'CD58', 'CD66c', 'CD10', 'CD38'],
        'ALL2':['CD45', 'CD19', 'CD34', 'sKappa', 'cIgM', 'CD33', 'sIgM+CD117', 'sLambda'],
        'ALL3':['CD45', 'CD19', 'CD34', 'CD9', 'cTdT', 'CD13', 'CD22', 'CD24'],
        'ALL4':['CD45', 'CD19', 'CD34', 'CD21', 'CD15+CD65', 'NG2', 'CD123', 'CD81'],
        'ALL5':['CD45', 'CD19', 'CD34', 'CD44', 'cTdT', 'CD99', 'EPOR', 'CD86'],
        'ALL6':['CD45', 'CD19', 'CD34', 'CD20', 'sCD3', 'sCD79a', 'CD22', 'CD10'],
        'Hairy Cell 1':['CD45', 'CD19', 'CD103', 'CD11c', 'CD5', 'sCD3', 'CD22', 'CD25'],
        'Hairy Cell 2':['CD45', 'CD19', 'CD103', 'sKappa', 'CD5', 'CD3', 'CD22', 'sLambda'],
        'IgG':['CD45', 'CD19', 'IgG'],
        'IgM':['CD45', 'CD19', 'sIgM'],
        'IgA':['CD45', 'CD19', 'IgA'],
        'IgD':['CD45', 'CD19', 'IgD'],
        'CD52':['CD45', 'CD19', 'CD52', 'sCD3'],
        }

    # iterate through the tube_list and search for keys in the tube_dict, return values added to analyte_list

    for tube in tube_list:

        list = tube_dict.get(tube)
        if list is not None:
            analyte_list.extend(list)

        # final tube list

    all_tubes = str(tube_list).replace('[','').replace(']','').replace('\'', '')

        # define analyte order

    analyte_order = ['CD1a', 'CD2', 'cCD3', 'sCD3', 'CD4', 'CD5', 'CD7', 'CD8', 'CD9', 'CD10', 'CD11b', 'CD11c', 'CD13', 'CD14', 'CD15', 'CD16', 'CD19', 'CD20', 'CD21', 'CD22', 'CD23', 'CD24', 'CD25', 'CD28', 'CD30', 'CD33', 'CD34', 'CD35', 'CD36', 'CD38', 'CD41', 'CD42a+CD61', 'CD42b', 'CD44', 'CD45', 'CD52', 'CD56', 'CD57', 'CD58', 'CD61', 'CD64', 'CD65', 'CD66c', 'CD71', 'cCD79a', 'sCD79a', 'CD81', 'CD86', 'CD99', 'CD103', 'CD105', 'CD117', 'CD123', 'CD138', 'CD203c', 'CD235a', 'CD300e', 'CD15+CD65', 'EPOR', 'FMC7', 'HLA-DR', 'IgA', 'IgD', 'IgG', 'cIgM', 'sIgM','sIgM+CD117', 'cKappa', 'sKappa', 'cLambda', 'sLambda', 'cMPO', 'NG2', 'TCRa/b', 'TCRg/d', 'cTdT']


        #create a loop to put analytes in order

    for analyte in analyte_order:
        if analyte in analyte_list:
            analyte_set.append(analyte)

    # make the analyte set printable

    analyte_str = str(analyte_set).replace('[','').replace(']','').replace('\'', '')

        # get analyte_count

    analyte_count = str(len(analyte_set))

    start_response("200 OK", [("Content-Type", "text/html")])

    if len(all_tubes) > 0:
        template = env.get_template('bill.html')
        template = template.render(all_tubes = all_tubes, analyte_str = analyte_str, analyte_count = analyte_count)
        yield(template.encode("utf8"))
    else:
        index_temp = env.get_template('index.html')
        yield(index_temp.render().encode('utf8'))
