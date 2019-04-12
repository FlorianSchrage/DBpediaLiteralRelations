### IMPORTANT NOTEBOOKS ###

(Notebooks not listed are just responsible for creating lookup objects (see list below).)

- Classify: 								Takes the formerly created training .csv files (data folder), re-balances the data and tries to train a classifier for each of them if possible. Prints the performance or stores the final models.

- Create_trainings: 						Creates the training .csv files (data folder) for classification. All features are created and the entire tagging and matching logic is included.
					
- Filter_mappingbased_literals:				Creates our triples file only containing literals for relations we want to consider. Also creates some lookup dicts.

- Generate_candidate_datasets:				Creates the candidate .csv files to be predicted by the trained classifiers.

- Infer_unit_conversion_formula:			Tries to infer unit conversion formula based on the training files (data folder).

- Predict_candidate_instances:				Adds the label to the candidate datasets using the trained classifiers and creates the new triples.

- Result_evaluator:							Script for manual result evaluation.

- Sort_mappingbased_literals_by_relation:	Takes the filtered triples file and sorts it by relation.


### FOLDER STRUCTURE ###

(Many folders are initially empty and get filled when executing the respective notebooks. The initial DBpedia files are required for that.)

/								All notebooks

/data							Training data .csv files

/data/candidates				Candidate data .csv files

/objects						All objects used by several notebooks (see list below)

/objects/data_info				Metadata for training data .csv files 

/objects/data_info/candidates	Metadata for candidate data .csv files

/objects/models					Scikit-learn classification models

/utils							Some useful methods used by several notebooks


### CREATED OBJECTS ###

- abstract_dict:				Dict, maps entity -> abstract text (e.g. '<http://dbpedia.org/resource/Astronomer>' -> 'An astronomer is a scientist in the field of astronomy who ...')

- candidate_dict:				Dict, maps relation -> list of entities that do not have a fact for this relation but are in the domain (e.g. '<http://dbpedia.org/ontology/area>' -> ['<http://dbpedia.org/resource/Algeria>', '<http://dbpedia.org/resource/Andorra>', ...])

- date_dict:					Dict, maps entity -> list of tuples containing (a tuple containing the date and its format) and (the start position of this date within the abstract)
								(e.g. '<http://dbpedia.org/resource/Alain_Connes>' -> [(('1947-04-01', 'ymd'), 39), ...]) ('y', 'ym' or 'ymd')

- domain_dict:					!!!Dict, maps relation -> class of its domain (can be OWL-defined or infered) (e.g. 'http://dbpedia.org/ontology/birthDate' -> 'http://dbpedia.org/ontology/Person')

- float_proportion_dict:		Dict, maps relation -> proportion of facts that contain real floats (only float relations!) (e.g. '<http://dbpedia.org/ontology/area>' -> 0.6104)

- instance_types_dict:			Dict, maps entity -> list of all its types/classes (e.g. '<http://dbpedia.org/resource/Alabama>' -> ['<http://dbpedia.org/ontology/PopulatedPlace>', '<http://dbpedia.org/ontology/Place>', ...])

- instance_types_reverse_dict: 	Dict, maps type/class -> list of all entities that are an instance of the class (e.g. '<http://dbpedia.org/ontology/PopulatedPlace>' -> ['<http://dbpedia.org/resource/Alabama>', '<http://dbpedia.org/resource/Andorra>, ...]')

- negative_dict:				Dict, maps relation -> True if relation is allowed to store negative values, False otherwise - only numeric relations! (e.g. '<http://dbpedia.org/ontology/area>' -> False)

- relation_stat_dict:			Dict, maps relation -> tuple containing mean and standard deviation of all relation's values (e.g. '<http://dbpedia.org/ontology/absoluteMagnitude>' -> (12.65395332398317, 48.99052040003584)) (Mean, Stdev)

- relation_type_dict:			!!!Dict, maps relation -> type (e.g. 'http://dbpedia.org/ontology/argueDate' -> 'http://www.w3.org/2001/XMLSchema#date')

- relations_cnt:				Counter, counts how often a relation occurs in the original triples file

- relations_valid:				List, all relations that have a type we want to consider (number or date)

- relations_invalid:			List, all relations that have a type we don't want to consider (e.g. String)

- spacy_date_dict:				Dict, maps relation -> list of tuples containg start-/end-indices of all dates found by SpaCy's NE-Tagger

- types_cnt:					Counter, counts how often a type (String, double etc.) occurs

- types_date:					List, all types that are generally dates

- types_float:					List, all types that are generally floating point numbers

- types_int:					List, all types that are generally integers

- types_invalid:				List, all types we don't want to consider (e.g. String)

- types_valid:					List, all types we want to consider (number or date)

- unit_conversion_dict:			Dict, maps tuple (from_unit, to_unit, T/F) to conversion factor or False
								If tuple[2] is False, we get an heuristic/infered result, containing the factor and the R^2 of the regression (e.g. ('km2', 'm2', False) -> (999927.759, 0.994))
								If tuple[2] is False and from_unit is not a unit actually (set from a manual evaluation), we do not get the tuple but False (e.g. ('square', 'km2', False) -> False)
								If tuple[2] is True, we get the manually created result, only containing the factor (e.g. ('km2', 'm2', True) -> 1000000.0)
								
- unit_dict:					Dict, maps relation -> unit in which values are measured (as String, taken from the label) or None if no unit (e.g '<http://dbpedia.org/ontology/area>' -> 'm2')

- unit_reverse_dict:			Dict, maps unit -> list of relations whose values are measured in this unit (e.g. 'm2' -> ['<http://dbpedia.org/ontology/area>', '<http://dbpedia.org/ontology/areaLand>' ...]