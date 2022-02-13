# Week 6 Year 1 Quiz

### Quiz Instructions

In this Week 6 Quiz, we will ask you a few questions about the ABCD substance use assessments and the Neuroimaging Data Model (NIDM) semantic markup.

***

## ABCD (substance use assessments) Questions

**Question 1**

The ABCD substance use interview includes questions about: (check all that apply)

- [ ] which substances youth have heard of
- [ ] subjective effects of early use (alcohol, nicotine, cannabis)
- [ ] problem symptoms related to use (alcohol, nicotine, cannabis)
- [ ] peer substance use and availability of substances in the neighborhood
- [ ] parent substance use and family history of use
- [ ] caffeine consumption and over-the-counter medications


**Question 2**

The goals of the ABCD substance use module include the characterization of: (check all that apply)

- [ ] risk and resilience factors for substance use and SUD development (e.g., early substance use attitudes, expectancies, subjective effects, peer use, parental rules)
- [ ] the impact of polysubstance use patterns and “gateway interactions” between different substances
- [ ] the consequences of repeated substance use on neurocognitive, emotional, and physical development
- [ ] associations between substance use and psychopathology
- [ ] differential trajectories of substance use initiation, experimentation, and use patterns


**Question 3**

Biospecimens (e.g., saliva, hair, and urine samples) provide a more objective measure of recent substance use and exposure. Biospecimen samples are collected for **ALL** participants enrolled in the ABCD Study at each in-person visit.

- True
- False

**Question 4**

Which of the following are examples of gating in the ABCD substance use interview? (check all that apply)

- [ ] In years baseline-2 year follow-up, a participant indicates they have “heard of” a given substance, additional questions about that particular substance will follow
- [ ] If a participant indicates they have heard of a potential “gateway” substance, additional questions about other substances will follow
- [ ] If a participant indicates they have NOT used a given substance, zeros may be inserted for any follow-up questions triggered by this question
- [ ] If a participant has indicated they have used a given substance, they will be asked to recall details of their first experience with that substance at future visits


**Question 5**

The Timeline Follow Back asks about detailed month-by-month substance use (i.e., date of use, amount in standard units) and applicable follow-up questions for some substances such as cannabis (e.g., route of administration) for the 12-month period preceding the interview date.

- True
- False


## ReproNim NIDM data questions

### Prerequisites

1. You have already [forked](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) and [cloned](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository): https://github.com/ABCD-ReproNim/sample_dataset
    - Enrolled students are encouraged to do this on the ABCD-ReproNim JupyterHub.
    - Observer students will have to do so on their own machines
2. You have installed [pynidm](https://pynidm.readthedocs.io/en/latest/) and [pyontutils](https://pypi.org/project/pyontutils/) (or are using our JupyterHub)
    - [notes on running JupyterHub locally for observer students](https://neurostars.org/t/using-abcd-repronim-jupyterhub-container-locally-via-docker/17439)

**Question 6**

How does structured data annotation help the research process? (Select all that apply)

- [ ] Can make filtering information within and between datasets easier
- [ ] Can reduce ambiguity about the measures recorded in a dataset
- [ ] Can give a better understanding about how data were acquired and processed
- [ ] Can help generate research hypotheses

<details>
<summary>Click to see answer</summary>

- Can make filtering information within and between datasets easier
- Can reduce ambiguity about the measures recorded in a dataset
- Can give a better understanding about how data were acquired and processed
- Can help generate research hypotheses

***

</details>

**Question 7**

[Register for an account on scicrunch](https://scicrunch.org/register?referer=%22%2F%22).
After you create an account and log in, click on "MY ACCOUNT" -> "API Keys".
On the API page, click "Generate an API key", and this should generate an API key.
(An API key is a unique identifier used to authenticate a user or a project to get access to a resource, in this
case you need authentication to get access to the unique terms and definitions that describe our data, such as `age` and `sex`.)
Under Project Name, type "abcd-repronim course", and then click update text.
To make the API key accessible for the next questions, make an environment variable (a variable stored within the shell you’re using)
in your terminal by typing:

- `export INTERLEX_API_KEY="YOUR_API_KEY"`

where "YOUR_API_KEY" is replaced with your actual API key
from scicrunch.
You can see if you were successful by typing `echo $INTERLEX_API_KEY` into your terminal. If you see your
API key printed in the terminal, you succeeded!
This step is necessary to get access to Universal Resource Locators (URLs)
that reference unique terms to disambiguate the measures recorded in our `sample_dataset`.
Once you have successfully created the API key and created the environment variable
`INTERLEX_API_KEY` in your terminal, paste the **LAST 4 CHARACTERS**
of your API Key as evidence of your success (do not share your entire API-key with
anyone).

- Enter last 4 characters

<details>
<summary>Click to see answer</summary>

Everyone's answer will be different,
example: `ah87`

***

</details>

**Question 8**

We will be working within BIDS formatted files for the following questions. You can read more about what BIDS is [here](https://github.com/bids-standard/bids-starter-kit/wiki/The-BIDS-folder-hierarchy) and how metadata (e.g. the “.tsv” and “.json” files we’ll be referencing in this question) are stored in BIDS format [here](https://github.com/bids-standard/bids-starter-kit/wiki/Metadata-file-formats).


While we already have a `participants.json` file in `sample_dataset` annotating
`age`, `sex`, and `handedness`; they do not link to URLs.
As Dr. David Keator mentioned in his lecture, `age` could refer to age at scan, or
age at first episode of psychosis, or age at last concussion, or many other
ambiguous meanings.
Luckily, `pynidm` can help us annotate `age`, `sex`, and `handedness` to include
URLs and reduce the ambiguity of the terms.

Assuming you are in the `sample_dataset` directory and have `pynidm` installed,
use the `bidsmri2nidm` command to add URLs to the variables in `participants.json`.
For the age variable, select `Chronological Age` and select `Genotypic Sex` for the sex variable, but you can select your favorite for `handedness`.

(**NOTE**: The `bidsmri2nidm` command will also annotate `pheno1.json` and `pheno2.json`
which contain redundant information, so it is expected that you will be annotating the
same variables multiple times).

Which of the following `bidsmri2nidm` commands below will annotate this dataset and
output a `nidm.ttl` file? (assuming you are in
the `sample_dataset` directory)

- `bidsmri2nidm -d nidm.ttl -o ${PWD} -bidsignore`
- `bidsmri2nidm -d ${PWD} -o nidm.ttl -bidsignore`
- `bidsmri2nidm -o ${PWD} -bidsignore`
- `bidsmri2nidm -d ${PWD} -bidsignore`

<details>
<summary>Click to see answer</summary>

`bidsmri2nidm -d ${PWD} -o nidm.ttl -bidsignore`

**Explanation**
- `bidsmri2nidm -d nidm.ttl -o ${PWD} -bidsignore`
    - `-d` represents the directory and `-o` represents
      the output file name, so the arguments are flipped.
    - `bidsmri2nidm -o ${PWD} -bidsignore`
        - missing the `-d` flag
    - `bidsmri2nidm -d ${PWD} -bidsignore`
        - missing the `-o` flag
- Here is the output of `bidsmri2nidm --help`
```
    usage: bidsmri2nidm [-h] -d DIRECTORY [-jsonld] [-bidsignore] [-no_concepts] [-json_map JSON_MAP] [-log LOGFILE] [-o OUTPUTFILE]

    This program will represent a BIDS MRI dataset as a NIDM RDF document and provide user with opportunity to annotate
    the dataset (i.e. create sidecar files) and associate selected variables with broader concepts to make datasets more FAIR. 

    Note, you must obtain an API key to Interlex by signing up for an account at scicrunch.org then going to My Account
    and API Keys.  Then set the environment variable INTERLEX_API_KEY with your key. 

    optional arguments:
    -h, --help            show this help message and exit
    -d DIRECTORY          Full path to BIDS dataset directory
    -jsonld, --jsonld     If flag set, output is json-ld not TURTLE
    -bidsignore, --bidsignore
                            If flag set, tool will add NIDM-related files to .bidsignore file
    -no_concepts, --no_concepts
                            If flag set, tool will no do concept mapping
    -log LOGFILE, --log LOGFILE
                            Full path to directory to save log file. Log file name is bidsmri2nidm_[basename(args.directory)].log
    -o OUTPUTFILE         Outputs turtle file called nidm.ttl in BIDS directory by default..or whatever path/filename is set here

    map variables to terms arguments:
    -json_map JSON_MAP, --json_map JSON_MAP
                            Optional full path to user-suppled JSON file containing variable-term mappings.
```

***

</details>

**Question 9**

Oh no! We forgot to include the Montreal Cognitive Assessment (MOCA) in `participants.tsv`.
The data are below.

| MOCA |
|------|
| 29   |
| 28   |
| 27   |
| 26   |
| 27   |

Open `participants.tsv` in your favorite editor and add the above information.
Now run the same `bidsmri2nidm` command that you ran in **Question 8** and you
will see a new variable (MOCA) you can annotate.

You will be asked a series of questions to annotate MOCA:
- Please enter a full name to associate with the term [MOCA]: Montreal Cognitive Assessment
- Please enter a definition for this term:  screening assessment for detecting cognitive impairment
- Please enter the datatype [1:11]: 4
    - the score is an integer
- Please enter the minimum value [NA]: 0
- Please enter the maximum value [NA]: 30
- Please enter the units [NA]: points

The next question asks for Concept Association, but the provided options are not very good:
```
Concept Association
Query String: MOCA
InterLex:

1: Label: MocA protein, Bacteroides fragilis     Definition:     Preferred URL: http://id.nlm.nih.gov/mesh/2018/M0221391
2: Label: MocA protein, Rhizobium meliloti       Definition:     Preferred URL: http://id.nlm.nih.gov/mesh/2018/M0242430
3: Label: Moca-cyp protein, Drosophila   Definition:     Preferred URL: http://id.nlm.nih.gov/mesh/2018/M0443056
4: Narrow Interlex query
5: Change query string from: "MOCA"
6: No concept needed for this variable
---------------------------------------------------------------------------------------
Please select an option (1:6) from above:
```
- Select 5 to change the query string
- Please input new search string for CSV column: MOCA     : Montreal Cognitive Assessment

Now you should have a better list of options.
Select the option labeled "Cognitive Assessment Screening Instrument".

If everything went successfully, the command should gracefully exit and `participants.json`
should be updated.

As evidence of successful completion, select the URL associated with MOCA in `participants.json`

- http://uri.interlex.org/base/ilx_0102162
- http://id.nlm.nih.gov/mesh/2018/M000620928
- http://id.nlm.nih.gov/mesh/2018/M0446358
- http://uri.interlex.org/base/ilx_0102339

<details>
<summary>Click to see answer</summary>

http://id.nlm.nih.gov/mesh/2018/M000620928

***

</details>

**Question 10**

With annotations complete, we can query our dataset!
While it may not be too exciting to only query our dataset, keep in mind this is a tool
that can query across many datasets, so you can select participants from a variety of datasets that meet particular
criteria for your research purposes.
In this example query, we will get the IDs of all Males in this dataset, using the sparql query below:
```
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix prov: <http://www.w3.org/ns/prov#>
prefix ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
prefix fsl: <http://purl.org/nidash/fsl#>
prefix nidm: <http://purl.org/nidash/nidm#>
prefix onli: <http://neurolog.unice.fr/ontoneurolog/v3.0/instrument.owl#>
prefix freesurfer: <https://surfer.nmr.mgh.harvard.edu/>
prefix dx: <http://ncitt.ncit.nih.gov/Diagnosis>
prefix ants: <http://stnava.github.io/ANTs/>
prefix dct: <http://purl.org/dc/terms/>
prefix dctypes: <http://purl.org/dc/dcmitype/>
prefix ncicb: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
prefix ncit: <http://ncitt.ncit.nih.gov/>

select distinct ?ID ?SEX
where {


            ?tool_act a prov:Activity ;

                    prov:qualifiedAssociation [prov:agent [ndar:src_subject_id ?ID]] .

                        ?as_activity prov:qualifiedAssociation [prov:agent ?agent] ;
                                        dct:isPartOf/dct:isPartOf [dctypes:title ?study] .
                        ?agent ndar:src_subject_id ?ID .


  # find sex data element uuid
                        {?sex_measure a nidm:DataElement ;
                                        nidm:isAbout <http://id.nlm.nih.gov/mesh/2018/M0446358> .
                        }


  ?as_entity prov:wasGeneratedBy ?as_activity ;

             ?sex_measure ?sex_coded .

             bind(IF(?sex_coded ="M"^^xsd:string , "M"^^xsd:string,"F"^^xsd:string) as ?SEX) .
  filter (?SEX = "M"^^xsd:string) .

  }
```
This sparql query is based on [this example query](https://github.com/dbkeator/simple2_NIDM_examples/blob/7cd4bb2e6d202080c2dcb2f81a5bc47280f486f6/queries/male_subj_IDs.sparql)

Copy and paste the above code into a file named `male_subj_IDs.sparql`.

Using the `nidm.ttl` file you created in the previous questions we will query this dataset.
Which of the commands below will run our query on the dataset?

- `pynidm visualize -nl nidm.ttl -q male_subj_IDs.sparql`
- `pynidm query -nl male_subj_IDs.sparql -q nidm.ttl`
- `pynidm query -nl nidm.ttl -q male_subj_IDs.sparql`
- `pynidm query -nl male_subj_IDs.sparql`
- `pynidm query -nl nidm.ttl`

If all goes well you should see this output:
```
       ID SEX
0  sub-03   M
1  sub-04   M
```

<details>
<summary>Click to see answer</summary>

`pynidm query -nl nidm.ttl -q male_subj_IDs.sparql`

**Explanation**
Here is the output from `pynidm query --help`:
```
Usage: pynidm query [OPTIONS]

  This function provides query support for NIDM graphs.

Options:
  -nl, --nidm_file_list TEXT      A comma separated list of NIDM files with
                                  full path  [required]

  -nc, --cde_file_list TEXT       A comma separated list of NIDM CDE files
                                  with full path. Can also be set in the
                                  CDE_DIR environment variable

  Query Type: [mutually_exclusive, required]
                                  Pick among the following query type
                                  selections

    -q, --query_file FILENAME     Text file containing a SPARQL query to
                                  execute

    -p, --get_participants        Parameter, if set, query will return
                                  participant IDs and prov:agent entity IDs

    -i, --get_instruments         Parameter, if set, query will return list of
                                  onli:assessment-instrument:

    -iv, --get_instrument_vars    Parameter, if set, query will return list of
                                  onli:assessment-instrument: variables

    -de, --get_dataelements       Parameter, if set, will return all
                                  DataElements in NIDM file

    -debv, --get_dataelements_brainvols
                                  Parameter, if set, will return all brain
                                  volume DataElements in NIDM file along with
                                  details

    -bv, --get_brainvols          Parameter, if set, will return all brain
                                  volume data elements and values along with
                                  participant IDs in NIDM file

    -gf, --get_fields TEXT        This parameter will return data for only the
                                  field names in the comma separated list
                                  (e.g. -gf age,fs_00003) from all nidm files
                                  supplied

    -u, --uri TEXT                A REST API URI query
  -o, --output_file TEXT          Optional output file (CSV) to store results
                                  of query

  -j / -no_j                      Return result of a uri query as JSON
  -v, --verbosity TEXT            Verbosity level 0-5, 0 is default
  --help                          Show this message and exit.
  ```

***

</details>
