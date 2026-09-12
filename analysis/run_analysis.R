# =============================================================================
# run_analysis.R
# PYROS rapid review: depressive symptoms in skilled migrants who restart a
# career versus recent graduates who migrate before establishing one.
#
# What this script does
#   Reads two files only: extraction/extraction.csv and extraction/quality.csv.
#   Writes Table 1, Table 2, a direction tally and Figures 1-3 into outputs/.
#   Nothing is typed in by hand: every number in every output comes from a row
#   of extraction.csv (protocol section 11, CLAUDE.md rule 3).
#
# How to run
#   Open analysis/analysis.Rproj in RStudio, then:  source("run_analysis.R")
#   Or from a terminal in the project root:         Rscript analysis/run_analysis.R
#
# Line-by-line notes are written as comments above each block.
# =============================================================================


# --- 1. Packages --------------------------------------------------------------
# library() loads a package for this session. tidyverse bundles readr (reading
# CSV), dplyr (filtering and summarising), tidyr (reshaping), stringr (text)
# and ggplot2 (figures). gt makes publication tables and saves them as HTML.
library(tidyverse)
library(gt)


# --- 2. Locate the project root -----------------------------------------------
# The script may be run from analysis/ (RStudio project) or from the project
# root (Rscript). This block finds the folder that contains "extraction/" so
# that file paths work in both cases.
# getwd() returns the current working directory as text.
root <- getwd()
# If "extraction" is not a folder here, step up one level with dirname().
if (!dir.exists(file.path(root, "extraction"))) root <- dirname(root)
# stopifnot() halts with a clear message if the folder is still missing.
stopifnot("extraction/ folder not found" = dir.exists(file.path(root, "extraction")))

# file.path() joins folder names with the correct separator for the system.
in_extraction <- file.path(root, "extraction", "extraction.csv")
in_quality    <- file.path(root, "extraction", "quality.csv")
out_tables    <- file.path(root, "outputs", "tables")
out_figures   <- file.path(root, "outputs", "figures")

# dir.create() makes the output folders; showWarnings = FALSE keeps it quiet
# if they already exist; recursive = TRUE creates parent folders as needed.
dir.create(out_tables,  showWarnings = FALSE, recursive = TRUE)
dir.create(out_figures, showWarnings = FALSE, recursive = TRUE)


# --- 3. Read the data ---------------------------------------------------------
# read_csv() reads a CSV into a tibble (a modern data frame).
# col_types = cols(.default = "c") reads every column as text first, so that
# nothing is silently coerced; the numeric columns are converted explicitly
# below. show_col_types = FALSE suppresses the column-type printout.
extraction <- read_csv(in_extraction,
                       col_types = cols(.default = "c"),
                       show_col_types = FALSE)
quality <- read_csv(in_quality,
                    col_types = cols(.default = "c"),
                    show_col_types = FALSE)

# Convert the columns that hold numbers. mutate() adds or changes columns;
# across() applies the same function to several columns; as.numeric() turns
# text like "21.9" into the number 21.9 and an empty cell into NA (missing).
extraction <- extraction |>
  mutate(across(c(year, sample_size, prevalence, mean_score,
                  effect_estimate, ci_low, ci_high), as.numeric))

# A derived column with the scale name only (the text before the first space
# or bracket in `measure`), used to group prevalence points by instrument.
# str_extract() pulls the first match of a regular expression:
#   ^            start of the text
#   [A-Za-z0-9-]+ one or more letters, digits or hyphens (e.g. "PHQ-9", "BDI")
extraction <- extraction |>
  mutate(scale = str_extract(measure, "^[A-Za-z0-9-]+"))

# A short label used on every figure: study id plus first author and year,
# e.g. "S039 Schilgen et al. 2020". paste() glues text together.
# For S172 (two samples) the country is appended so the two rows differ.
extraction <- extraction |>
  group_by(study_id) |>
  mutate(label = if (n() > 1) paste(study_id, authors, year, country)
                 else paste(study_id, authors, year)) |>
  ungroup()

# Direction of the finding, taken from the sentence beginning "Direction:" in
# `notes`. The regular expression "Direction: ([^.]+)" captures everything
# after "Direction: " up to the next full stop. str_match() returns a matrix;
# column 2 is the captured group.
extraction <- extraction |>
  mutate(direction_text = str_match(notes, "Direction: ([^.]+)")[, 2])


# --- 4. Quality flags ---------------------------------------------------------
# Turn the five yes/no/unclear answers into one compact string per study,
# e.g. "Y/N/?/N/N", for Table 1. case_when() maps each answer to a symbol.
flag <- function(x) case_when(x == "yes" ~ "Y", x == "no" ~ "N", TRUE ~ "?")

quality_flags <- quality |>
  mutate(quality_flags = paste(flag(q1_sampling_representative),
                               flag(q2_validated_measure),
                               flag(q3_migrant_type_clear),
                               flag(q4_response_rate_ge50),
                               flag(q5_adjusted_age_sex_stay),
                               sep = "/")) |>
  select(study_id, quality_flags)


# --- 5. Table 1: study characteristics ----------------------------------------
# left_join() adds the quality flags to each extraction row by study_id.
# select() keeps and orders the columns the protocol lists for Table 1.
table1 <- extraction |>
  left_join(quality_flags, by = "study_id") |>
  select(study_id, authors, year, country, design, sample_size,
         migrant_type, measure, quality_flags) |>
  arrange(study_id)

# write_csv() saves the plain data; gt() builds the formatted table and
# gtsave() writes it as HTML for the report.
write_csv(table1, file.path(out_tables, "table1_study_characteristics.csv"))

table1 |>
  gt() |>
  tab_header(title = "Table 1. Characteristics of included studies") |>
  cols_label(study_id = "ID", authors = "Authors", year = "Year",
             country = "Destination", design = "Design", sample_size = "n",
             migrant_type = "Migrant type", measure = "Measure",
             quality_flags = "Quality (Q1-Q5)") |>
  tab_source_note("Quality flags: Q1 sampling representative; Q2 validated measure; Q3 migrant type clear; Q4 response rate >= 50%; Q5 adjusted for age, sex and length of stay. Y = yes, N = no, ? = unclear. Source: extraction/extraction.csv and extraction/quality.csv.") |>
  gtsave(file.path(out_tables, "table1_study_characteristics.html"))


# --- 6. Table 2: findings by migrant type -------------------------------------
# One row per extraction row. The CI is shown as one text column built with
# if_else(): when there is no estimate the cell stays blank rather than "NA".
table2 <- extraction |>
  mutate(ci_95 = if_else(is.na(effect_estimate), "",
                         paste0(ci_low, " to ", ci_high))) |>
  select(study_id, authors, year, migrant_type, measure, prevalence,
         mean_score, effect_estimate, ci_95, direction_text) |>
  arrange(migrant_type, study_id)

write_csv(table2, file.path(out_tables, "table2_findings_by_migrant_type.csv"))

table2 |>
  gt() |>
  tab_header(title = "Table 2. Findings by migrant type") |>
  cols_label(study_id = "ID", authors = "Authors", year = "Year",
             migrant_type = "Migrant type", measure = "Measure and cut-off",
             prevalence = "% above cut-off", mean_score = "Mean score",
             effect_estimate = "Effect estimate", ci_95 = "95% CI",
             direction_text = "Direction (from notes)") |>
  sub_missing(missing_text = "") |>
  tab_source_note("Effect estimates are of different types (see notes column of extraction.csv) and are not comparable across rows. Mean scores are on different scales and must not be compared across studies.") |>
  gtsave(file.path(out_tables, "table2_findings_by_migrant_type.html"))


# --- 7. Direction tally -------------------------------------------------------
# The protocol asks for a count of comparative studies that support H1,
# contradict H1, or show no difference. H1 concerns professionals versus
# recent graduates. No included study makes that comparison, so the tally is
# reported with the comparator each study actually used. The comparator and
# the category are assigned here, in plain sight, from the study's notes.
# case_when() reads like a list of "if this, then that" rules; the first rule
# that is TRUE wins.
direction_tally <- extraction |>
  mutate(
    comparator = case_when(
      study_id == "S039" ~ "native-born nurses",
      study_id == "S075" ~ "native-born nurses",
      study_id == "S107" ~ "other immigrant occupational groups",
      study_id == "S139" ~ "control group (before-after)",
      study_id == "S159" ~ "immigrants with no change in social status",
      study_id == "S172" ~ "the other forced-migrant sample",
      TRUE ~ "none"
    ),
    h1_comparison = "no (professional vs recent graduate not tested)",
    finding = case_when(
      str_detect(direction_text, regex("no difference|no change", ignore_case = TRUE)) ~ "no difference",
      str_detect(direction_text, regex("lowest", ignore_case = TRUE)) ~ "professionals lower than comparator",
      str_detect(direction_text, regex("status-loss|mismatch|underemployment", ignore_case = TRUE)) ~ "more symptoms with status loss or underemployment",
      TRUE ~ "no comparator"
    )
  ) |>
  select(study_id, migrant_type, comparator, h1_comparison, finding, direction_text)

write_csv(direction_tally, file.path(out_tables, "direction_tally.csv"))

# count() gives the number of rows in each finding category.
direction_counts <- direction_tally |> count(finding, name = "n_rows")
write_csv(direction_counts, file.path(out_tables, "direction_tally_counts.csv"))


# --- 8. Figure 1: prevalence by migrant type ----------------------------------
# Keep rows that report a prevalence. filter() drops rows where the value is
# missing (is.na()).
fig1_data <- extraction |>
  filter(!is.na(prevalence))

# ggplot() starts a plot; aes() maps columns to visual properties.
# geom_point() draws one point per study row; facet_wrap() splits the panel
# by scale so that different instruments are never mixed on one axis.
fig1 <- ggplot(fig1_data,
               aes(x = prevalence, y = label, colour = migrant_type)) +
  geom_point(size = 4) +
  # geom_text() prints the value next to each point; nudge_y lifts it a little.
  geom_text(aes(label = paste0(prevalence, "%")), nudge_y = 0.3, size = 3.5,
            show.legend = FALSE) +
  facet_wrap(~ measure, ncol = 1, scales = "free_y") +
  # xlim() fixes the axis from 0 to 100 so panels are comparable in scale.
  xlim(0, 100) +
  labs(title = "Figure 1. Percent above the depressive-symptom cut-off",
       subtitle = "One point per study sample; each panel is a different instrument or cut-off; not pooled",
       x = "Percent above cut-off", y = NULL, colour = "Migrant type",
       caption = "Source: extraction/extraction.csv (column: prevalence)") +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom")

# ggsave() writes the figure; width and height are in inches; dpi sets sharpness.
ggsave(file.path(out_figures, "fig1_prevalence_by_migrant_type.png"), fig1,
       width = 9, height = 6, dpi = 200, bg = "white")


# --- 9. Figure 2: effect estimates with 95% CI --------------------------------
# Keep rows with an effect estimate. The estimate type is read from the notes:
# rows whose notes mention "OR" are odds ratios (null value 1, log axis);
# rows mentioning "difference" are mean differences (null value 0).
fig2_data <- extraction |>
  filter(!is.na(effect_estimate)) |>
  mutate(
    estimate_type = case_when(
      str_detect(notes, "adjusted OR") ~ "Odds ratio (null = 1)",
      str_detect(notes, "difference")  ~ "Mean difference (null = 0)",
      TRUE ~ "Other"
    ),
    null_value = if_else(str_detect(estimate_type, "Odds"), 1, 0)
  )

# geom_errorbar() with orientation = "y" draws the horizontal CI bar (the
# older geom_errorbarh() is deprecated in ggplot2 4.0); geom_vline() draws the null
# line for each panel; facet_wrap(scales = "free") lets each estimate type
# keep its own axis. No pooled estimate is drawn (protocol section 11).
fig2 <- ggplot(fig2_data,
               aes(x = effect_estimate, y = label)) +
  geom_vline(aes(xintercept = null_value), linetype = "dashed", colour = "grey40") +
  geom_errorbar(aes(xmin = ci_low, xmax = ci_high), width = 0.2, orientation = "y") +
  geom_point(aes(colour = migrant_type), size = 4) +
  geom_text(aes(label = paste0(effect_estimate, " (", ci_low, " to ", ci_high, ")")),
            nudge_y = 0.3, size = 3.5) +
  facet_wrap(~ estimate_type, ncol = 1, scales = "free") +
  labs(title = "Figure 2. Effect estimates with 95% confidence intervals",
       subtitle = "Each estimate is against the comparator stated in the study notes; no pooling",
       x = "Estimate", y = NULL, colour = "Migrant type",
       caption = "Source: extraction/extraction.csv (columns: effect_estimate, ci_low, ci_high)") +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom")

ggsave(file.path(out_figures, "fig2_effect_estimates.png"), fig2,
       width = 9, height = 5, dpi = 200, bg = "white")


# --- 10. Figure 3: explanatory factors named across studies -------------------
# factors_named holds items separated by ";". separate_rows() turns each item
# into its own row. str_trim() removes spaces at the ends. A factor is
# protective if its bracketed text starts with "(protective"; the bracket is then
# removed with str_remove() so that "social_support (protective)" and
# "social_support" count as the same factor.
fig3_data <- extraction |>
  select(study_id, factors_named) |>
  separate_rows(factors_named, sep = ";") |>
  mutate(factors_named = str_trim(factors_named)) |>
  filter(factors_named != "") |>
  mutate(role = if_else(str_detect(factors_named, "\\(protective"),
                        "Protective", "Risk-increasing"),
         factor = str_trim(str_remove(factors_named, "\\(.*\\)"))) |>
  # distinct() makes sure one study counts a factor once at most.
  distinct(study_id, factor, role) |>
  count(factor, role, name = "n_studies")

# geom_col() draws bars; fct_reorder() sorts factors by how often they appear.
fig3 <- ggplot(fig3_data,
               aes(x = n_studies, y = fct_reorder(factor, n_studies, .fun = sum),
                   fill = role)) +
  geom_col() +
  scale_x_continuous(breaks = 0:10) +
  labs(title = "Figure 3. Explanatory factors named in the included studies",
       subtitle = "Number of studies naming each factor, split by direction",
       x = "Number of studies", y = NULL, fill = NULL,
       caption = "Source: extraction/extraction.csv (column: factors_named)") +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom")

ggsave(file.path(out_figures, "fig3_factors_named.png"), fig3,
       width = 9, height = 6, dpi = 200, bg = "white")

# Save the counts behind Figure 3 as well, so the report can quote them.
write_csv(fig3_data, file.path(out_tables, "fig3_factor_counts.csv"))


# --- 11. Finish ---------------------------------------------------------------
# cat() prints a short confirmation so the user can see the run completed.
cat("Done. Outputs written to", file.path(root, "outputs"), "\n")
cat("Rows analysed:", nrow(extraction), "| studies:", n_distinct(extraction$study_id), "\n")
