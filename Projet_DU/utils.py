from IPython.display import display, HTML
import pandas as pd
import numpy as np

#cette fonction permit d'afficher un SVG sur Jupyter le code .js je l'ai trouvé sur internet
def pygal_show(obj):
  base_html = """
    <!DOCTYPE html>
    <html>
      <head>
      <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
      <script type="text/javascript" src="https://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js"></script>
      </head>
      <body>
        <figure>
          {rendered_chart}
        </figure>
      </body>
    </html>
    """
  return display(HTML(base_html.format(rendered_chart=obj.render(is_unicode=True))))

#cette fonction est utilisée pour mettre l'header d'un pivot table à un seul niveau
#remarque la varibale 'dep' est une variable local

def unif_header(base):
    base.index.name=None
    base['dep']=base.index
    base=base.rename_axis(None, axis=1).reset_index(drop=True)
    return

#Les Fonctions de Netoyage

def cleaner_Num_Acc(base: pd.DataFrame):
    base.drop_duplicates(subset='Num_Acc', keep='last',inplace=True)
    base.reset_index(drop=True,inplace=True)
    return  

def cleaner_vit(base : pd.DataFrame):
    base.loc[(base.vit=="Inc"),"vit"]=np.nan
    base['vit'] = pd.to_numeric(base['vit'],errors = 'coerce')
    base.loc[(base.vit>=250),"vit"]=250
    base.vit.fillna(base['vit'].mean(),inplace=True)
    return

def cleaner_circ(base : pd.DataFrame):
    base.loc[base.circ==-1,"circ"]=base.circ.median()
    base.loc[base.circ==np.nan,"circ"]=base.circ.median()
    return  

def cleaner_vosp(base : pd.DataFrame):
    base.loc[base.vosp==-1,"vosp"]=base.vosp.median()
    base.loc[base.vosp==np.nan,"vosp"]=base.vosp.median()
    return  

def cleaner_prof(base : pd.DataFrame):
    base.loc[base.prof==-1,"prof"]=base.prof.median()
    base.loc[base.prof==np.nan,"prof"]=base.prof.median()
    return  

def cleaner_plan(base : pd.DataFrame):
    base.loc[base.plan==-1,"plan"]=base.plan.median()
    base.loc[base.plan==np.nan,"plan"]=base.plan.median()
    return 

def cleaner_surf(base : pd.DataFrame):
    base.loc[base.surf==-1,"surf"]=base.surf.median()
    base.loc[base.surf==np.nan,"surf"]=base.surf.median()
    return 

def cleaner_situ(base : pd.DataFrame):
    base.loc[base.situ==-1,"situ"]=base.situ.median()
    base.loc[base.situ==np.nan,"situ"]=base.situ.median()
    return 

def cleaner_nbv(base : pd.DataFrame):
    base['nbv'] = pd.to_numeric(base['nbv'],errors = 'coerce')
    base.loc[base.nbv==0,"nbv"]=np.nan
    base.loc[base.nbv==-1,"nbv"]=np.nan
    base.loc[base.nbv==np.nan,"nbv"]=base.nbv.median()
    return

def cleaner_vma(base : pd.DataFrame):
    base.loc[(base.vma>=0) &(base.vma<30),"vma"]=30
    base.loc[(base.vma>=130),"vma"]=130
    base.loc[base.vma<0,"vma"]=np.nan
    base.loc[base.vma.isnull(),"vma"]=base.vma.median()
    return

#cette fonction remplace les septs fonction avec colonne=['circ', 'nbv', 'vosp', 'prof','plan','surf', 'situ']
def cleaner_colonne(base : pd.DataFrame,colonne):
    base.loc[base[colonne]==-1,colonne]=base[colonne].median()
    base.loc[base[colonne]==np.nan,colonne]=base[colonne].median()
    return 

def cleaner_PEC(base : pd.DataFrame):
    base['PriseEnCharge']=base['PriseEnCharge'].apply(lambda x : x.replace(',','.'))
    base['PriseEnCharge']=pd.to_numeric(base['PriseEnCharge'],errors = 'coerce')
    return

def diagnostic(base,var):
    a=base[var].value_counts()
    b=base[var].isnull().sum()
    c=base[var].isna().sum()
    return print(a,"////",var,"////",b,"////",c,"////",base.dtypes[var])