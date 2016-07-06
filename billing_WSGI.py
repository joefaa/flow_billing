import jinja2
import cgi
from reagent_list import analyte_order, tube_dict

def application(environ, start_response):
    # This line tells the template loader where to search for template files
    templateLoader = jinja2.FileSystemLoader( searchpath="./" )

    # This creates your environment and loads a specific template
    env = jinja2.Environment(loader=templateLoader)
    template = env.get_template('bill.html')

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

    # iterate through the tube_list and search for keys in the tube_dict, return values added to analyte_list

    for tube in tube_list:

        list = tube_dict.get(tube)
        if list is not None:
            analyte_list.extend(list)

        # final tube list

    all_tubes = str(tube_list).replace('[','').replace(']','').replace('\'', '')

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
        result = "The following analytes were tested ({0}): {1}. (Total {2})".format(all_tubes, analyte_str, analyte_count)
        template = template.render(result = result)
        yield(template.encode("utf8"))
    else:
        result = ""
        template = template.render(result = result)
        yield(template.encode("utf8"))

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
