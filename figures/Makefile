DATA_DIR := ../data
FIGURE_DIR := .
SRC_DIR := .

# figures to generate

figures = figure-task-switching-replication-accuracy \
	figure-task-switching-replication-reaction-time

figure_results := $(patsubst %, $(FIGURE_DIR)/%.png, $(figures))


## List of all valid targets in this sub project:
## ----------------------------------------------
## all        : By default run all figure generation tasks
##              if the figures are out of date.
##
.PHONY : all
all : $(figure_results)


## figure-task-switching-replication-reaction-time.png
##            : Create a bar graph summarizing the
##              reaction time subject data broken down
##              by posture and congruancy conditions.
##
stroop_replication_files = \
	task-switching-replication
stroop_replication_data := $(patsubst %, $(DATA_DIR)/%.csv, $(stroop_replication_files))

$(FIGURE_DIR)/figure-task-switching-replication-reaction-time.png: $(SRC_DIR)/visualize-task-switching-replication-reaction-time.py $(stroop_replication_data)
	python $^ --output $@


## figure-task-switching-replication-accuracy.png
##            : Create a bar graph summarizing the
##              accuracy subject data broken down
##              by posture and congruancy conditions.
##
$(FIGURE_DIR)/figure-task-switching-replication-accuracy.png: $(SRC_DIR)/visualize-task-switching-replication-accuracy.py $(stroop_replication_data)
	python $^ --output $@


## clean      : DANGER: Remove all generated figures.  Figure generation is relatively
##              quick, so actually removing and redoing all figures is not that big a deal
##              if needed.
##
.PHONY : clean
clean  :
	rm -rf $(figure_results) *~

## help       : Get all build targets supported by this build.
##
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
