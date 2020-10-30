import Icon, { IconSize, IconType } from 'app/common/components/icon/icon';
import { QAMetricsData } from 'app/common/store/qa-metrics/types';
import React from 'react';

import "./predictions-table.scss";
import cn from "classnames";
import Tooltip from "app/common/components/tooltip/tooltip";

interface IProps {
	tableData: QAMetricsData[];
	totalCount: number;
	onChangePage: (pageIndex: number, limit: number) => void;
}

interface IState {
	limit: number;
	currentPage: number;
}

class PredictionsTable extends React.Component<IProps, IState> {
	state = {
		limit: 20,
		currentPage: 1,
	};

	onChangeLimit = (e: React.ChangeEvent<HTMLSelectElement>) => {
		const newLimit = Number(e.target.value);
		const oldLimit = this.state.limit;
		let newCurrentPage = Math.ceil((this.state.currentPage * oldLimit) / newLimit);

		if ((newCurrentPage - 1) * newLimit > this.props.totalCount)
			newCurrentPage = Math.ceil(this.props.totalCount / newLimit);

		this.setState({
			limit: newLimit,
			currentPage: newCurrentPage,
		});
		this.props.onChangePage(newCurrentPage, newLimit);
	};

	setPage = (newPage: number) => () => {
		this.setState({
			currentPage: newPage,
		});
		this.props.onChangePage(newPage, this.state.limit);
	};

	// TODO: refactor method to function
	determineColor = (value: string): string => {
		switch (value) {
			case "Won’t Fixed":
				return "green";
			case "Not Won’t Fixed":
				return "dark-blue";

			case "Rejected":
				return "orange";
			case "Not Rejected":
				return "violet-dark";

			case "0–30 days":
				return "cold";
			case "31–90 days":
				return "yellow-strong";
			case "91–180 days":
				return "orange";
			case "> 180 days":
				return "light-red";

			default:
				return "default";
		}
	};

	render() {
		const { tableData } = this.props;

		const columnsNames: string[] = Object.keys(tableData[0]);

		return (
			<div className="predictions-table">
				{this.renderTableHeader()}

				{/* for top fixed table header */}
				<table className="predictions-table__table predictions-table__table_with-head">
					<thead>
						<tr>
							{columnsNames.map((columnName, index) => (
								<th key={index}>{columnName}</th>
							))}
						</tr>
					</thead>

					<tbody>
						{tableData.map((item, index) => (
							<tr key={index}>
								{columnsNames.map((columnName, index) => (
									<td key={index}>{String(item[columnName])}</td>
								))}
							</tr>
						))}
					</tbody>
				</table>

				{/* data table */}
				<div className="predictions-table__scrollable-container">
					<table className="predictions-table__table predictions-table__table_with-body">
						<thead>
							<tr>
								{columnsNames.map((columnName, index) => (
									<th key={index}>{columnName}</th>
								))}
							</tr>
						</thead>

						<tbody>
							{tableData.map((item, index) => (
								<tr key={index}>
									{columnsNames.map((columnName, index) => {
										const str = String(item[columnName]);

										const charActualWidth = 10; // Actual average width of symbols with font-size 16px
										const isTooltipDisplayed =
											str.replace(/\W/g, "").length * charActualWidth > 400; // if sum width of all symbols larger than td max-width than display tooltip

										return (
											<td
												key={index}
												className={`color_${this.determineColor(String(item[columnName]))}`}
											>
												<Tooltip message={str} isDisplayed={isTooltipDisplayed}>
													<p
														className={cn({
															"predictions-table__table-cell-title": isTooltipDisplayed,
														})}
													>
														{str}
													</p>
												</Tooltip>
											</td>
										);
									})}
								</tr>
							))}
						</tbody>
					</table>
				</div>
			</div>
		);
	}

	renderTableHeader = () => {
		const { currentPage, limit } = this.state;

		const rowFrom = (currentPage - 1) * limit + 1;
		let rowTo = currentPage * limit;

		const totalPage = Math.ceil(this.props.totalCount / limit);

		if (rowTo > this.props.totalCount) {
			rowTo = this.props.totalCount;
		}

		return (
			<div className="predictions-table__pagination predictions-table-pagination">
				<div className="predictions-table-pagination__field">
					<span className="predictions-table-pagination__label">Show by</span>

					<select
						className="predictions-table-pagination__select"
						value={this.state.limit}
						onChange={this.onChangeLimit}
					>
						<option value={20}>20</option>
						<option value={50}>50</option>
						<option value={100}>100</option>
					</select>
					<Icon type={IconType.down} size={IconSize.small} className="predictions-table-pagination__select-icon"/>
				</div>

				<div className="predictions-table-pagination__field">
					<span className="predictions-table-pagination__label">Shown</span>

					{totalPage > 1 && (
						<button
							onClick={this.setPage(currentPage - 1)}
							disabled={currentPage === 1}
							className="predictions-table-pagination__button"
						>
							<Icon type={IconType.left} size={16} className="predictions-table-pagination__icon" />
						</button>
					)}

					<div>
						<span className="predictions-table-pagination__value">
							{rowFrom}-{rowTo}
						</span>
						<span className="predictions-table-pagination__label">of</span>
						<span className="predictions-table-pagination__value">{this.props.totalCount}</span>
					</div>

					{totalPage > 1 && (
						<button
							onClick={this.setPage(currentPage + 1)}
							disabled={currentPage === totalPage}
							className="predictions-table-pagination__button"
						>
							<Icon
								type={IconType.right}
								size={16}
								className="predictions-table-pagination__icon"
							/>
						</button>
					)}
				</div>
			</div>
		);
	};
}

export default PredictionsTable;
