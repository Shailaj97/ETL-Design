CREATE TABLE raw_timesheet(
	id  SERIAL UNIQUE,
	employee_id VARCHAR(200),
	department_id VARCHAR(200),
	shift_start_time TIME,
	shift_end_time TIME,
	shift_date DATE,
	shift_type VARCHAR(200),
	hours_worked FLOAT,
	attendance BOOLEAN,
	has_taken_break BOOLEAN,
	break_hour FLOAT,
	was_charge BOOLEAN,
	charge_hour FLOAT,
	was_on_call BOOLEAN,
	on_call_hour FLOAT,
	num_teammates_absent INT
)